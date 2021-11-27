# Register your models here.
from django.contrib import admin
from .models import Blog
from django.db import models

#admin.site.register(Project)


@admin.register(Blog)
class AuthorAdmin(admin.ModelAdmin):
    pass
