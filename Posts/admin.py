from django.contrib import admin
from .models import Member , Group, Like
# Register your models here.

admin.site.register(Member)
admin.site.register(Group)
admin.site.register(Like)
