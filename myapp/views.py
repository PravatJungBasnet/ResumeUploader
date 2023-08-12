from django.shortcuts import render
from .forms import Resumeuploader
from .models import Resume

# Create your views here.
def resumeup(request):
    if request.method=='POST':
        
        fm=Resumeuploader(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    else:
       
        fm=Resumeuploader()
    candidates=Resume.objects.all()
    
    
    
    return render(request,'myapp/home.html',{'form':fm,'candidate':candidates})
def showdet(request,id):
    pi=Resume.objects.get(pk=id)
    return render(request,'myapp/candidate.html',{'pro':pi})
  

    
