from django.shortcuts import render,redirect
from . import models

def main(request): # barcha ma'lumotlarni olamiz
    service=models.Service.objects.all()
    doctors=models.Doctors.objects.all()
    clients=models.Client.objects.all()
    # o'zgaruvchiga saqlab olamiz
    context={
        'service':service,
        'doctors':doctors,
        'clients':clients

    }

    return render(request, 'index.html',context)


def service(request): # Alohida pageda ishlatish uchun ma'lumotlarni olamiz
    service=models.Service.objects.all()
    return render(request, 'service.html',{'service':service})


def doctor(request):# Alohida pageda ishlatish uchun ma'lumotlarni olamiz
    doctors=models.Doctors.objects.all()
    return render(request, 'about.html',{'doctors':doctors})


def client(request):# Alohida pageda ishlatish uchun ma'lumotlarni olamiz
    clients=models.Client.objects.all()
    return render(request,'blogs.html',{'clients':clients})


def contact(request): # contact funksiyasi ishlaganda contact.html ga o'tib ketadi
    if request.method=='POST':
        models.Contact.objects.create(
            fulname=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['text']
        )
        

    return render(request,'contact.html')

