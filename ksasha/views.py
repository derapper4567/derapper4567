from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from typing import Any
from .models import ksasha

def myhome(request):
    members = ksasha.objects.all()

    return render(request,'home.html',{'members':members})
def Register(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Reg_no = request.POST.get('Reg_no')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:  # Password validation check
            # Create the new user
            user = User.objects.create_user(username=username, password=password)
            # Save the additional details to the ksasha model
            member = ksasha.objects.create(name=name, email=email, Reg_no=Reg_no, user=user)
            return redirect('success')  # Redirect to a success page
        
        else:
            return render(request, 'Register.html', {'error': 'Passwords do not match'})

    return render(request, 'Register.html')
def login_user(request: Any) ->Any:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            message.info(request,'Invalid Username or Password')
            return redirect('login_user')
    else:
         return render(request,"login.html")



