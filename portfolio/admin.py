from django.contrib import admin
from .models import Project
from django.db import models

#admin.site.register(Project)


@admin.register(Project)
class AuthorAdmin(admin.ModelAdmin):
    pass
