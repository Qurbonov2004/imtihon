from django.db import models
#Service uchun class yozib olamiz
class Service(models.Model):    
    icon=models.ImageField()
    name=models.CharField(max_length=200)
    about=models.CharField(max_length=200)

    class Meta():
        verbose_name_plural='Xizmatlar'

#doktorlar uchun class yozib olamiz
class Doctors(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)

    class Meta():
        verbose_name_plural='Shifokorlar'

#Foydalanuvchi fikrini olish uchun uchun class yozib olamiz
class Client(models.Model):
    icon=models.ImageField()
    message=models.TextField()
    name=models.CharField(max_length=200)
    profession=models.CharField(max_length=200)

    class Meta():
        verbose_name_plural='mijozlar fikri'


#Bog'lanish  uchun class yozib olamiz
class Contact(models.Model):
    fulname=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

    class Meta():
        verbose_name_plural="Biz bilan bog'laning"


    
        
