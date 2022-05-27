""" A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; see Making queries. """



from django.db import models

from django.contrib.auth.models import User


""" user_directory_path(instance, filename) - returns the path fo the faculty image requested """
def user_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = instance.firstname + instance.lastname
    filename = name +'.'+ ext 
    return 'Faculty_Images/{}'.format(filename)


"""student_directory_path(instance,filename) - returns the path of the student image requested"""
def student_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = instance.registration_id # + "_" + instance.branch + "_" + instance.year + "_" + instance.section
    filename = name +'.'+ ext 
    return 'Student_Images/{}/{}/{}/{}'.format(instance.branch,instance.year,instance.section,filename)


""" @class Faculty-maps data to 'attendence_sys_faculty' table"""
class Faculty(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=user_directory_path ,null=True, blank=True)

    def __str__(self):
        return str(self.firstname + " " + self.lastname)



""" @class Student - maps data to 'attendence_sys_student' table"""
class Student(models.Model):

    BRANCH = (
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('CHEM','CHEM'),
        ('MECH','MECH'),
        ('EEE','EEE'),
    )
    YEAR = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    SECTION = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    registration_id = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    year = models.CharField(max_length=100, null=True, choices=YEAR)
    section = models.CharField(max_length=100, null=True, choices=SECTION)
    profile_pic = models.ImageField(upload_to=student_directory_path ,null=True, blank=True)


    def __str__(self):
        return str(self.registration_id)


""" @class Attendence - maps data to 'attendence_sys_attedence' table"""
class Attendence(models.Model):
    Faculty_Name = models.CharField(max_length=200, null=True, blank=True)
    Student_ID = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add = True, null = True)
    time = models.TimeField(auto_now_add=True, null = True)
    branch = models.CharField(max_length=200, null = True)
    year = models.CharField(max_length=200, null = True)
    section = models.CharField(max_length=200, null = True)
    period = models.CharField(max_length=200, null = True)
    status = models.CharField(max_length=200, null = True, default='Absent')

    def __str__(self):
        return str(self.Student_ID + "_" + str(self.date)+ "_" + str(self.period))