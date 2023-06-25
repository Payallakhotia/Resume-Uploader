from django.db import models

state_choices = (
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chandigarh","Chandigarh"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Lakshadweep","Lakshadweep"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Odisha","Odisha"),
    ("Puducherry","Puducherry"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
)

class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=state_choices,max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)

