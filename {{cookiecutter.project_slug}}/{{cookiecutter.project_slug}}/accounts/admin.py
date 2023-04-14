from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.list_filter += ("bio", "avatar")
UserAdmin.fieldsets += (("Extra Fields", {"fields": ("bio", "avatar")}),)

admin.site.register(User, UserAdmin)
