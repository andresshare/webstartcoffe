from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home',{})

def about(request):
    return render(request,'about',{})

def services(request):
    return render(request,'services',{})

def store(request):
    return render(request,'store',{})

def contact(request):
    return render(request,'store',{})

def blog(request):
    return render(request,'blog',{})

 def sample(request):
    return render(request,'sample',{})             