from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "index.html")

def explore(request):
    return render(request, "explore.html")

def details(request):
    return render(request, "details.html")

def create(request):
    return render(request, "create.html")

def author(request):
    return render(request, "author.html")