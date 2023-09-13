from django.contrib import admin
from .models import Mymodel

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username','password')

# Register your models here.
admin.site.register(Mymodel,LoginAdmin)