from django.db import models



# Created model name 'Post' to upload memes  
class Post(models.Model):
    user=models.CharField(max_length=200)
    caption=models.TextField()
    URL=models.URLField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user
