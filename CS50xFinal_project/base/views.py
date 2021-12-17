from django.shortcuts import render, HttpResponse


# Create your views here.
def Home(request):
    return render(request, "base/home.html", context={
        "resualt":None,
    })

def Specialities(request):
    return render(request, "base/specialities.html", context={
        "resualt":None,
    })

def Expriences(request):
    return render(request, "base/experiences.html", context={
    "resualt":None,
    })

def Academy(request):
    return render(request, "base/academy.html", context={
    "resualt":None,
    })

def Contact(request):
    return render(request, "base/contact.html", context={
    "resualt":None,
    })

def Bio(request):
    return render(request, "base/Bio.html", context={
    "resualt":None,
    })

def CV(request):
    return render(request, "base/CV.html", context={
    "resualt":None,
    })

def Profile(request):
    return render(request, "base/profile.html", context={
    "resualt":None,
    })

def LogIn(request):
    return render(request, "base/login.html", context={
    "resualt":None,
    })
