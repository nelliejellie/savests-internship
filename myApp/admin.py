from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#rename the admin header
admin.site.site_header = 'SAVEST INTERNSHIP'

# Unregister the provided model admin
admin.site.unregister(User)

# Register our UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name','username','is_active')
    list_editable = ['is_active']
    

# Register your models here.


