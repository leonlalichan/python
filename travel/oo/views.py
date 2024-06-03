from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib import messages



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            return render(request, 'login.html')

    return render(request, 'login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        f = request.POST['first_name']
        l = request.POST['last_name']
        e = request.POST['email']
        p = request.POST['password']
        c = request.POST['confirm_password']

        if p == c:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')

            elif User.objects.filter(email=e).exists():
                messages.info(request, "Email taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=p, last_name=l, first_name=f, email=e)
                user.save()
                messages.info(request, "User created")
                return redirect('/')
        else:
            messages.info(request, "Passwords do not match")
            return render(request, 'register.html')
    return render(request, "register.html")
