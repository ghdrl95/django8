from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(PostType)
admin.site.register(Image)
admin.site.register(File)