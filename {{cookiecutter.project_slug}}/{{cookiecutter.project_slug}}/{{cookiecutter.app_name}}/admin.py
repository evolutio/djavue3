from django.contrib import admin

from .models import ActivityLog, {{cookiecutter.model_singular}}


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class {{cookiecutter.model_singular}}Admin(admin.ModelAdmin):
    list_display = ('description', 'done')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register({{cookiecutter.model_singular}}, {{cookiecutter.model_singular}}Admin)
