# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
# 
# .

from django.contrib import admin
from .models import Post

admin.site.register(Post)