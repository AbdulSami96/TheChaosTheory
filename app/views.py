from django.shortcuts import render
from django.http import HttpResponse
from app.models import contactdetails
from app.models import Product
from app.models import productinfo
from app.models import review
from django.core.mail import send_mail

# Create your views here.  

def reviews(request):
    if request.method == "POST":
        savest = review()
        savest.name = request.POST.get("name")
        savest.review = request.POST.get("review")
        savest.save()
        return render(request,"reviews.html")
    else:
        return render(request,"reviews.html")  

def index(request):
    result = Product.objects.all()
    results = review.objects.all()
    return render(request, 'index.html',{"Product":result,"review":results}) 

def about(request):
    return render(request, 'about.html')

def chefs(request):
    return render(request, 'chefs.html')

def events(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def menu(request):
    result = Product.objects.all()
    return render(request, 'menu.html',{"Product":result})
    
def details(request, id):
    result = productinfo.objects.filter(id=id)
    return render(request, 'details.html',{"productinfo":result})

def specials(request):
    return render(request, 'specials.html')

def contact(request):
    if request.method == "POST":
        savest = contactdetails()
        savest.Name = request.POST.get("name")
        savest.Email = request.POST.get("email")
        savest.Message = request.POST.get("message")
        savest.PhoneNumber = request.POST.get("phone")
        send_mail(
            "Contact Us",
            savest.Message,
            savest.Email,
            ['samplew33@gmail.com']
        )
        savest.save()
        return render(request,"contact.html")
    else:
        return render(request,"contact.html")    






