from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    sub_title = models.TextField()
    post = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return f"{self.title} , {self.slug}"
class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_num = models.IntegerField()
    mess = models.TextField()
    date = models.DateTimeField()
    def __str__(self): 
        return f"{self.name} , {self.email}"