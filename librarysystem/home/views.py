from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages\index.html')
def demo(request):
    return render(request, 'demo.html')

def books(request):
    return render(request, 'pages\books.html')