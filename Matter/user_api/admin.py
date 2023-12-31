from django.contrib import admin
from user.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

# ------------------MODIFICATION REQUIRED------------------------------
class UserAdminConfig(UserAdmin): # check the link to see why we use UserAdmin https://docs.djangoproject.com/en/4.1/topics/auth/customizing/

    model = CustomUser

    list_display = ('id','email', 'username', 'first_name' ,'last_name', 'balance', 'is_active',
     'is_staff', 'is_superuser') #Set list_display to control which fields are displayed on the admin page
    ordering = ('id',) #Set ordering to specify how lists of objects should be ordered in the Django admin views
    search_fields = ('email', 'username', 'first_name', 'last_name') #Set search_fields to enable a search box on the admin change list page
    list_filter = ('is_active', 'is_staff', 'is_superuser') #Set list_filter to activate filters in the right sidebar of the change list page of the admin.

    add_fieldsets = (
        (None,      {'classes': ['wide'], 
                     'fields': ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']}
        ), 
    ) #add_fieldsets (for fields to be used when creating a user)

    fieldsets = (
        (None,          {'fields': ('email', 'username', 'first_name', 'last_name')}),
        ('Permission',  {'fields': ('is_staff', 'is_active', 'is_superuser')}),

    ) #fieldsets (for fields to be used in editing users)



        
admin.site.register(CustomUser, UserAdminConfig)