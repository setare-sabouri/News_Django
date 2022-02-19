from pyexpat import model
from django.db import models
from django.contrib.auth.models import User #for author



class News(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True) #tarikh ghyre ghabel taghier tavasot user
    image = models.ImageField(default='def.jpg',blank=True)
    #connect 2 models with forienKey , User and News
    author=models.ForeignKey(User, default=None,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
        
    def snippet(self):             #baes mishe matne Lorem tolani , kotah dide beshe
        return self.body[:20]+'...'