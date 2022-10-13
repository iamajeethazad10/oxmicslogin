from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
def Login(request):
    return render(request, 'login.html')




def Register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
            if User.objects.filter(email=email).exists():
                messages.error(request, "email already exists")
            else:
                user = User.objects.create(username=username,fname=fname, lname=lname, email=email,
                                           pass1=pass1)
                user.save()
                if user is not None:
                    auth.Login(request, user)
                    return HttpResponse("Registered Successfully and logged in")

        else:
            messages.error(request, "password doesnt match")

    else:
        return render(request, 'login.html')

