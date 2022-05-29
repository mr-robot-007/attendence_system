import os
from django.db import models


base_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir("..")
base_dir = os.getcwd()
image_dir = os.path.join(base_dir, "{}/{}/{}/{}/{}/{}".format(
    'static', 'images', 'Student_Images', 'CSE', 2, 'C'))
image_dir = image_dir+'/'+'1214.png'
print(image_dir)
os.remove(image_dir)
