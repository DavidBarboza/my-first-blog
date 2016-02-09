from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title