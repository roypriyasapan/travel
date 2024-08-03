from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def pakages(request):
    return render(request,'pakages.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def review(request):
    return render(request,'review.html')