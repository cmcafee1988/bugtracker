from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bugsapp.models import MyUser, Ticket

# Register your models here.
admin.site.register(MyUser, UserAdmin)
admin.site.register(Ticket)
