from tkinter import Widget
from django import forms
from django.forms import ModelForm

from .models import *

""" Forms in django allow user to generates html form - allows user to send or reciever data in forms. """
""" A ModelForm maps a model class’s fields to HTML form <input> elements via a Form; this is what the Django admin is based upon. """


""" The super() function is used to give access to methods and properties of a parent or sibling class.
    it returns an object that represents the parent class. """
    
""" visible_fields() - Return a list of BoundField objects that aren't hidden fields. The opposite of the hidden_fields() method. """


""" @class CreateStudentForm generates Student form """
class CreateStudentForm(ModelForm):
   
    class Meta:
        model = Student
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CreateStudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
    
""" @class FacultyForm geneates Faculty form """
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'    