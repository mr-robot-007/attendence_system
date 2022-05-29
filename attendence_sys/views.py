"""view functions are Python function that takes a Web request and returns a Web response. """


from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Student, Attendence
from .filters import AttendenceFilter

from .encoder import Encoder
from .recognizer import Recognizer

from datetime import date
import time

from threading import Thread

import xlwt
import os

""" global variables """
known_face_encodings =[]
known_face_names = []


""" home() - request = POST -> add/register new student if not registered
           - request = GET -> render home.html 
"""          
@login_required(login_url = 'login')  #allow access only if logged in
def home(request):
    studentForm = CreateStudentForm()

    if request.method == 'POST':
        studentForm = CreateStudentForm(data = request.POST, files=request.FILES)
        stat = False 
        try:
            student = Student.objects.get(registration_id = request.POST['registration_id'])  #check if registration_id already exist
            stat = True
        except:
            stat = False
        if studentForm.is_valid() and (stat == False):
            studentForm.save()  #save new student data to database
            
            Thread(target=call_encoder).start()  #generate encodings agains with new updated data
            time.sleep(1)
            name = studentForm.cleaned_data.get('firstname') +" " +studentForm.cleaned_data.get('lastname')
            messages.success(request, 'Student ' + name + ' was successfully added.')
            return redirect('home')
        else:
            messages.error(request, 'Student with Registration Id '+request.POST['registration_id']+' already exists.')
            return redirect('home')

    context = {'studentForm':studentForm}
    
    return render(request, 'attendence_sys/home.html', context)




"""
    call_encoder() - calls Encoder() function -> it is created to make async call to Encoder function using Thread
"""
def call_encoder():
    global known_face_encodings,known_face_names
    encodings,name= Encoder()
    known_face_encodings,known_face_names=encodings,name
    return




""" 
    loginPage() - check credentials and allow user to login only with correct credentials
"""
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    
    #if encodings aren't generated yet -> call Encoder()
    global known_face_encodings,known_face_names
    if(known_face_encodings==[]):
        Thread(target=call_encoder).start()
        
    return render(request, 'attendence_sys/login.html', context)  #render login.html




"""
    logoutUser() - allows user to logout only if logged in and return to login window
"""
@login_required(login_url = 'login')
def logoutUser(request):
    logout(request)
    return redirect('login')




"""
    updateStudentRedirect() - checks if reg_id for provided branch exits and redirect to updateStudent() if exists
"""
@login_required(login_url = 'login')
def updateStudentRedirect(request):
    context = {}
    if request.method == 'POST':
        try:
            reg_id = request.POST['reg_id']
            branch = request.POST['branch']
            student = Student.objects.get(registration_id = reg_id, branch = branch)
            updateStudentForm = CreateStudentForm(instance=student)  #updateStudent form for provided reg_id
            context = {'form':updateStudentForm, 'prev_reg_id':reg_id, 'student':student}
        except:
            messages.error(request, 'Student Not Found')
            return redirect('home')
        
    return render(request, 'attendence_sys/student_update.html', context)




""" updateStudent() - gets data from form and check if data entered is valid or not .
    If everything is correct shows message of success and call Encoder() . Returns to home.html
    else showes message of unsuccessful and redirect to home
"""
@login_required(login_url = 'login')
def updateStudent(request):
    if request.method == 'POST':
        context = {}
        try:
            student = Student.objects.get(registration_id = request.POST['prev_reg_id'])
            updateStudentForm = CreateStudentForm(data = request.POST, files=request.FILES, instance = student)
            
            details = {
            'id':request.POST['prev_reg_id'],
            'branch':request.POST['branch'],
            'year': request.POST['year'],
            'section':request.POST['section'],
            }
            base_dir = os.path.dirname(os.path.abspath(__file__))
            base_dir = os.getcwd()
            image_dir = os.path.join(base_dir, "{}/{}/{}/{}/{}/{}/{}".format(
                'static', 'images', 'Student_Images',details['branch'],details['year'],details['section'],details['id']))
            image_dir = image_dir +'.png'
            
            if updateStudentForm.is_valid():
                #delete old file
                if(os.path.isfile(image_dir)):
                    os.remove(image_dir)
                    
                updateStudentForm.save()
                messages.success(request, 'Updation Success')
                Thread(target=call_encoder).start()
                time.sleep(1)
                return redirect('home')
        except:
            messages.error(request, 'Updation Unsucessfull')
            return redirect('home')
        
    return render(request, 'attendence_sys/student_update.html', context)




"""
    takeAttedence() - accept detials(branch,year,period,faculty) from form and takes attendance for that class
"""
@login_required(login_url = 'login')
def takeAttendence(request):
    if request.method == 'POST':
        details = {
            'branch':request.POST['branch'],
            'year': request.POST['year'],
            'section':request.POST['section'],
            'period':request.POST['period'],
            'faculty':request.user.faculty
            }
        
        #checks if attendance for today is already 
        if Attendence.objects.filter(date = str(date.today()),branch = details['branch'], year = details['year'], section = details['section'],period = details['period']).count() != 0 :
            messages.error(request, "Attendence already recorded.")
            return redirect('home')
        else:
            students = Student.objects.filter(branch = details['branch'], year = details['year'], section = details['section'])
            global known_face_encodings,known_face_names
            time.sleep(1)
            
            #calls Recognizer() that returns the names(reg_id) of the recoginized students if they are student of that class
            names = Recognizer(known_face_encodings,known_face_names)
            for student in students:
                if str(student.registration_id) in names:
                    attendence = Attendence(Faculty_Name = request.user.faculty, 
                    Student_ID = str(student.registration_id), 
                    period = details['period'], 
                    branch = details['branch'], 
                    year = details['year'], 
                    section = details['section'],
                    status = 'Present')   #recognised and matched students marked present
                    attendence.save()   #saves attendance to DB
                else:
                    attendence = Attendence(Faculty_Name = request.user.faculty, 
                    Student_ID = str(student.registration_id), 
                    period = details['period'],
                    branch = details['branch'], 
                    year = details['year'], 
                    section = details['section'])
                    attendence.save()   #unrecognised students are marked absent
            
            #filter attendance of the current class and render on attendence.html
            attendences = Attendence.objects.filter(date = str(date.today()),branch = details['branch'], year = details['year'], section = details['section'],period = details['period'])
            context = {"attendences":attendences, "ta":True}
            messages.success(request, "attendence taking Success")
            return render(request, 'attendence_sys/attendence.html', context)    
            
    context = {}
    
    return render(request, 'attendence_sys/home.html', context)



"""
    searchAttendance() - takes details from form about filters(ex. year, branch, class, date,etc), filters data as per queryset and renders on attendance.html
"""
def searchAttendence(request):
    global attendences 
    attendences= Attendence.objects.all()       #gets all data from attendence_sys_attendence table
    myFilter = AttendenceFilter(request.GET, queryset=attendences)
    attendences = myFilter.qs       #filters data
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'attendence_sys/attendence.html', context)



"""
    facultyProfile() - loads data about logged in faculty and renders it on FacultyForm.html
"""
def facultyProfile(request):
    faculty = request.user.faculty
    form = FacultyForm(instance = faculty)
    context = {'form':form}
    return render(request, 'attendence_sys/facultyForm.html', context)



"""
    export_users_xls() - downloads the searched attendance in .xls file
"""
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="attendence.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('attendence Data') # this will make a sheet named attendence Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Student_ID', 'branch', 'year', 'section','date','period','status']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    global attendences
    rows = attendences.values_list('Student_ID', 'branch', 'year', 'section','date','period','status')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

