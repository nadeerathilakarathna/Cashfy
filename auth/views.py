from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    referring_url = request.META.get('HTTP_REFERER', None)
    if request.method == 'POST':
    # post_data = request.POST
    # for key, value in post_data.items():
    #     print(f"{key}, {value}")
        if referring_url:
                print(referring_url)
                if referring_url.split('/')[-1] == 'login':
                    print("LOGIN")
                    email = request.POST['email']
                    password = request.POST['password']
                    user = auth.authenticate( email=email, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect("dashboard")
                    else:
                        messages.info(request, 'invalid credentials')
                        return redirect('login')
                elif referring_url.split('/')[-1] == 'signup':
                    post_data = request.POST
                    for key, value in post_data.items():
                        print(f"{key}, {value}")


                return render(request, 'index.html')
    else:
        return render(request,'index.html')

def login(request):
    referring_url = request.META.get('HTTP_REFERER', None)
    if request.method == 'POST':
        print("LOGIN")
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate( username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('home')
    return redirect('home')

def signup(request):
    referring_url = request.META.get('HTTP_REFERER', None)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'email is taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
            else:
                user = User.objects.create_user(username=email, email=email,password=password1,first_name=firstname, last_name=lastname,)
                user.save()
                messages.info(request, 'user created. please signin.')
        else:
            messages.info(request, 'password does not match')
        return render(request, 'index.html')
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')