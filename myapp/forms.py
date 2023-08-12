from .models import Resume
from django import forms
GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]

class Resumeuploader(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    
    class Meta:
       
        model=Resume
        fields=('id','name', 'dob','gender', 'email','address','locality','city','pan', 'number','profile','file')
        labels={'dob':'DOB','pan':'PanNumber'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'address':forms.TextInput(attrs={'class':'form-control'}),
                 'pan':forms.NumberInput(attrs={'class':'form-control'}),
                 'locality':forms.TextInput(attrs={'class':'form-control'}),
                 'city':forms.Select(attrs={'class':'form-control'}),
                 'number':forms.NumberInput(attrs={'class':'form-control'}),
                 
                 
                 
                 
                 
                 
                 }
