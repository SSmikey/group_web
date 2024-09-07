from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return render(request, 'index.html')


def browsePage(request):
    return render(request, 'browse.html')


def detailsPage(request):
    return render(request, 'details.html')


def profilePage(request):
    return render(request, 'profile.html')


def streamsPage(request):
    return render(request, 'streams.html')
