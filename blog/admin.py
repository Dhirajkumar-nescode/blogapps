#Configuring the admin
#We are creating admin to add,edit and delete the post we've just modelled.
#Code given below means is used to add some bits from other file
from django.contrib import admin

#Now to edit the post we need to import our Post model from model 
from .models import Post

# Register your models here.
admin.site.register(Post)
