from django.shortcuts import render

# Create your views here.


def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):
    if request.method=='post':
        uname=request.POST.get('username')
    return render (request,'signup.html')



def LoginPage(request):
    return render (request,'login.html')
