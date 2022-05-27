# Face Verification Based Attendance System

## About
In this Attendance System the attendance for students is marked using Face verification. The Faculty has the permission to take Attendance, add a student, modify student details. The Faculty can also search for attendance of a student using Multiparameter Search, by specifying the student ID, date of attendance, period of Attendance.
The credentials for the Faculty are provided by the superuser who has access to the whole database. Only the superuser can update the attendance of a student.
Django web framework was used for the development of the whole web app. OpenCv and face_recognition API's were used for the development of Face Recognizer. The Face Recognizer can detect multiple faces at a time and mark their attendance into Database (sqlite3)


**Note: Python version 3.9 was used for this project. And the dlib package(already included) required for installation of face_recognition api is also uploaded.**

**Make sure python is installed and is added to PATH**

Download from here - https://www.python.org/downloads/

![alt text](https://www.tutorialspoint.com/assets/questions/media/49353/install_Python2.jpg)

**Visual Studio (Desktop Development with C++ ) must be installed**

Download from here - https://visualstudio.microsoft.com/downloads/

![alt text](https://github.com/mr-robot-007/attendence_system/blob/master/static/readme_files/visualstudio.png)

To install dlib cmake must be installed
```sh
pip install cmake
```
To run the web app on your local computer, install the required libraries(requirements.txt) using the command:

```sh
pip3 install -r requirements.txt
```

**Note -  while installing requirements.txt it can 5-10 mins to install all packages**

### Testing Credentials 
> username = tester | 
> password = engageprogram

### Create New User
To create your own credential for logging into the application run: 
```sh
python manage.py createsuperuser
```
After running the above command and creating the credentials, you can use the same credentials for logging in.
### To start the application run:
```sh
python manage.py runserver
```

**To create a faculty profile**

Navigate to Django admin page - http://127.0.0.1:8000/admin 
```sh
1. login using your credentials  
2. Go to Facultys in ATTENDENCE_SYS
3. Add Faculty 
4. In User, select the newly created User
5. Fill details and SAVE
```

Now you can login with as faculty with the credentials of the newly created user 

**Note***
1. Upload only clear image (with clear background) of the student and image should should not contain more than 1 face.
2. while adding or updating student details , make sure image files are in .png or .jpg format only
3. while Searching attendence with Date - add date in [YYYY-MM-DD] format.
4. While taking attendance - to save attendance or close camera window press 's' on the keyboard.




