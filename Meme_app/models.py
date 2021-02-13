from django.db import models



# Created model name 'Post' to upload memes  
class Post(models.Model):
    name=models.CharField(max_length=200)
    url=models.URLField(max_length=1000)
    caption=models.TextField()
   
    timestamp=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user
