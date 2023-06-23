from django.shortcuts import render
from . forms import studentregistration
from django.contrib import messages

# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm=studentregistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS,'your accout has been created !!!')
            messages.info(request,'you can login!!')
            messages.warning(request,'this is warning!!')
            messages.error(request,'this is request!!')
    else:
     fm=studentregistration()
    return render(request,'enroll/student.html',{'form':fm })
        
 