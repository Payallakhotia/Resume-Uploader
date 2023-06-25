from django import forms
from .models import Resume

gender_choices=[
    ('Male','Male'),
    ('Female','Female')
]

job_city_choice=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Ranchi','Ranchi'),
    ('Mumbai','Mumbai'),
    ('Dhanbad','Dhanbad'),
    ('Banglore','Banglore')
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred job locations',choices=job_city_choice,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields='__all__'
        labels={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No.','email':'Email ID','profile_image':'Profile Image','my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }