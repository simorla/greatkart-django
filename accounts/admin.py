from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from . models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','user_name','last_login','date_joined','is_active')
    list_display_links=('email','first_name','last_name')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    ordering=()


admin.site.register(Account,AccountAdmin)
