from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .form import formz,formz2,formz3
from .models import Login,Registration,Home
from django.contrib.auth.decorators import login_required
def login(request):
    form1 = formz()
    if request.method == 'POST':
        form1 = formz(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home_page')
    return render(request,"login.html",context={'form': form1})

def registration(request):
    form2 = formz2()
    if request.method == 'POST':
        form2 = formz2(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("login")
    return render(request,"register.html",context={'form': form2})

def home_page(request):
    form3 = formz3()
    if request.method == 'POST':
        form3 = formz3(request.POST)
        if form3.is_valid():
            Home = form3.save()
            name = request.POST.get('name')
            password = request.POST.get('password')
            Home.add_points_to_ancestors(10)
            return redirect('home')
    #         Home.objects.create(name=name)
    #         last_login = Login.objects.all().order_by('-si_number').first()
    #         si_number = (last_login.si_number + 1) if last_login else 1
    #         Login.objects.create(si_number=si_number, name=name, password=password)



    # logins = Login.objects.all().order_by('si_number')
    # return render(request,"home.html",{'logins':logins})
    return render(request, "home.html",{'form':form3})