from django.contrib import admin
from .models import Client, Contact,Doctors,Service

admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(Doctors)
admin.site.register(Service)
