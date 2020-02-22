from django.contrib import admin

# Register your models here.
from .models import User, Record
from services.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Record)
