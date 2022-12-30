#here we register any models that we wanna show in our admin panel
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)