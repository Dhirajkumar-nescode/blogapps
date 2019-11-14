from django.contrib import admin
from .models import Post
admin.site.register(Post)


"""
This file used for  Configuring the admin

1.This Code  is used to add some bits from other file
2.We have imported Post model defined in models.py 
3.To make our model visible on the admin page we need to register the model
with this code.

"""
