from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registersPage(request):
    return render(request, 'registers.html')

def profilePage(request):
    return render(request, 'profile.html')

def streamsPage(request):
    return render(request, 'streams.html')