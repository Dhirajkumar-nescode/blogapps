#Steps 6->
#This is place where we defined all objects call Models of our blog post and it is going yo save in the Database
#Code given below means is used to add some bits from other file
from django.conf import settings
from django.db import models
from django.utils import timezone


#Create Class for Blogspost.
#Identify properties of Blog.
#Properties of blogs are author,title,text,created_date,published_date
#Post is our name of the model.
#Always start a class name with uppercase.
#models.Models means that Post is Django model,so Django knows that it should be saved in the database.
class Post(models.Model):  
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#Define method called publish and the rules is always function/method name should be lowercase and with underscore instead of whitespace
#Method always return something 
#Both method is intended inside the class
    def publish(self):
        self.published_date = timezone.now()
        self.save()

#Whenever we call __str__, we will get a text with post title
    def __str__(self):
        return self.title


# Steps 7:Next step is to create the tables for models in your database