from django.contrib import admin

from .models import {{cookiecutter.model_singular}}


class {{cookiecutter.model_singular}}Admin(admin.ModelAdmin):
    list_display = ("description", "done")


admin.site.register({{cookiecutter.model_singular}}, {{cookiecutter.model_singular}}Admin)
