from django.contrib.auth.backends import UserModel
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from base.models import AboutMe, Experiences, contact, specialities
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
# Create your views here.
def Home(request):
    try:
        Bio_Model = AboutMe.objects.all()[0]
        Bio_Text  = Bio_Model.Bio
        Bio_Image = Bio_Model.image_address
        SPEIS = specialities.objects.all()
        experiences = Experiences.objects.all()
        academies = Academy.objects.all()
        return render(request, "base/home.html", context={
            "Bio" : Bio_Text,
            "Image_URL" : Bio_Image,
            "SPEIS" : SPEIS,
            "experiences":experiences,
            "academies":academies,
        })
    except IndexError:
        return render(request, "base/home.html", context={
            "resualt":"Failed",
        })

def Specialities(request):

    try:
        SPEIS = specialities.objects.all()
        return render(request, "base/specialities.html", context={
            "SPEIS" : SPEIS
        })         
    except IndexError:
        return render(request, "base/specialities.html", context={
            "resualt":None,
    })

def Expriences(request):
    try:
        experiences = Experiences.objects.all()
        return render(request, "base/experiences.html", context={
        "experiences":experiences,
        })
    except IndexError:
        return render(request, "base/experiences.html", context={
        "resualt":None,
        })
from base.models import Academy
def Academy_View(request):
    try:
        academies = Academy.objects.all()
        return render(request, "base/academy.html", context={
        "academies":academies,
        })
    except IndexError:
        return render(request, "base/academy.html", context={
        "resualt":None,
        })

#Take Contacts Messages To My Email
def Contact(request):
    if request.method == "POST":
        email   = request.POST["email"]
        message = request.POST["message"]
        contact.objects.create(Email = email, name = "Empty", Message = message)
        return render(request, "base/home.html", context={
            "resualt" : "message sent successfuly."
        })
    else:
        return render(request, "base/contact.html", context={
        "resualt":None,
        })

#Returnning the content Of Bio

def Bio(request):
    try:    
        Bio_Model = AboutMe.objects.all()[0]
        Bio_Text  = Bio_Model.Bio
        Bio_Image = Bio_Model.image_address
        print(f"Bio Text : {Bio_Text} \n Bio_Image : {Bio_Image} \n")
        return render(request, "base/Bio.html", context={
            "Bio" : Bio_Text,
            "Image_URL" : Bio_Image,
        })
    except IndexError:
        return render(request, "base/Bio.html", context={
            "Bio" : "DataBase Is Empty",
            "Image_URL" : "Database Is Empty",
        })

#Returning Response For CV Page
def CV(request):
    return render(request, "base/CV.html", context={
    "resualt":None,
    })

#Returning Response For Profile
@login_required(login_url="/LogIn")
def Profile(request):
    return render(request, "base/profile.html", context={
    "resualt":None,
    })


def LogIn(request):
    if request.method == "POST":
        username = request.POST["Username"]
        password = request.POST["password"]
        user     = authenticate (request, username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, "base/home.html", context={
                "LOGIN_Status":"You Loged_in Successfully!",
            })
        else:
            return render(request, "base/login.html", context={
            "resualt":"FAILED",
            }) 
    else:
        return render(request, "base/login.html", context={
        "resualt":None,
        })

def LogOut(request):
        logout(request)
        return redirect(Home)
    
    