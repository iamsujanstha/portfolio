from django.contrib import admin
from .models import Project, skill,tag
# Register your models here.
admin.site.register(Project)
admin.site.register(tag)
admin.site.register(skill)

