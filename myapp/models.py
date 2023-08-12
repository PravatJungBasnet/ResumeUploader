from django.db import models
STATE_CHOICE=[
    ('Kathmandu','Kathmandu'),
    ('Biratnagar','Biratnagar'),
    ('Pokhara','Pokhara'),
    ('Dharan','Dharan'),
    ('Chitwan','Chitwan'),
    ('Janakpur','Janakpur'),

]

# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=30)
    gender=models.CharField(max_length=20)
    pan=models.IntegerField(blank=True)
    locality=models.CharField(max_length=40)
    city=models.CharField(choices=STATE_CHOICE,max_length=30)
    number=models.IntegerField()
    profile=models.ImageField(upload_to='profileimg', blank=False)
    file=models.FileField(upload_to='doc',blank=False)

