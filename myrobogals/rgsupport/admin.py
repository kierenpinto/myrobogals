from django.contrib import admin

# Register your models here.
from .models import Request, Department, Department_Emails

admin.site.register(Request)
admin.site.register(Department)
admin.site.register(Department_Emails)