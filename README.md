# Face Recognition Based Attendance System

## About
This Project created during **MICROSOFT ENGAGE MENTORSHIP PROGRAM 2022**
In this Attendance System the attendance for students is marked using Face recognition. The Faculty has the permission to take Attendance, add a student, modify student details. The Faculty can also search for attendance of a student using Multiparameter Search, by specifying the student ID, date of attendance, period of Attendance.
The credentials for the Faculty are provided by the superuser who has access to the whole database. Only the superuser can update the attendance of a student.
Django web framework was used for the development of the whole web app. OpenCv and face_recognition API's were used for the development of Face Recognizer. The Face Recognizer can detect multiple faces at a time and mark their attendance into Database (sqlite3)

#### Reason to chose this project
I was already having experience of working with web application with Javascript frameworks.I had never worked on on Django or Open-CV earlier. I used to get fascinated bu Open-CV projects. So I find engage program as an opportunity to learn about Open-CV and build a project in intergration with Django.

## Technologies Used
- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Open-CV](https://opencv.org/)
- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [Sqlite3](https://www.sqlite.org/index.html)

## Pre-requisites
- Fundamentals of [Python](https://www.freecodecamp.org/news/python-fundamentals-for-data-science/) 
- Django 
    - [Models](https://docs.djangoproject.com/en/4.0/topics/db/models/) ,
    - [Connection with Database](https://docs.djangoproject.com/en/4.0/ref/databases/#sqlite-notes) 
    - [Forms](https://docs.djangoproject.com/en/4.0/ref/forms/)
    - [Filters](https://django-filter.readthedocs.io/en/stable/)
- Opencv - [Face recogniton using cv2](https://pyimagesearch.com/2018/09/24/opencv-face-recognition/)
- HTML,CSS - [Fundamentals](https://www.w3schools.com/html/)

## Architechture
![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/architechture.png)

Demo Video -[Youtube](https://youtu.be/Re4r04-tGXM

## Installation
1. Python should be should installed [Download from here - https://www.python.org/downloads/]
**Note:** 
    - **Python version 3.9 was used for this project. And the dlib package(already included) required for installation of face_recognition api is also uploaded.**
    - **Make sure python is installed and is added to PATH**




![alt text](https://www.tutorialspoint.com/assets/questions/media/49353/install_Python2.jpg)

2. Visual Studio with C++ (**for windows only**)

    Download from here - https://visualstudio.microsoft.com/downloads/

![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/visualstudio.png)

3. To install dlib cmake must be installed
    ```sh
    pip install cmake
    ```
4. Install the required libraries(requirements.txt) using the command:

    ```sh
    pip3 install -r requirements.txt
    ```

    **Note -  while installing requirements.txt it can 5-10 mins to install all packages**
# Usage
### Testing Credentials 
> username = tester | 
> password = engageprogram

### How to Create New User
To create your own credential for logging into the application run: 
```sh
for windows :python manage.py createsuperuser
for ubuntu : python3 manage.py createsuperuser
```
After running the above command and creating the credentials, you can use the same credentials for logging in.
### To start the application run:
```sh
for windows : python manage.py runserver
for ubuntu : python3 manage.py runserver
```

### **To create a faculty profile**

Navigate to Django admin page - http://127.0.0.1:8000/admin 
```sh
1. login using your credentials  
2. Go to Facultys in ATTENDENCE_SYS
3. Add Faculty 
4. In User, select the newly created User
5. Fill details and SAVE
```

Now you can login with as faculty with the credentials of the newly created user 

### **Note - while using the project**

1. Upload only clear image (with clear background) of the student and image should should not contain more than 1 face.
2. **Image should be in .png format**(faces will not be recognised for .jpg/.jpeg files) and **less than 1MB** in size.
3. *To convert images from jpg/jpeg to png format you can use - **https://cloudconvert.com/***
4. while adding or updating student details , make sure **image files are in .png** only
5. while Searching attendence with Date - enter **date in [YYYY-MM-DD] format**.
6. While taking attendance - **to save attendance** or close camera window **press 's' on the keyboard**.

## ScreenShots
![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/loginpage.png)
![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/homepage.png)
![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/updatestudentpage.png)
![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/searchattendance.png)
![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/account.png)


