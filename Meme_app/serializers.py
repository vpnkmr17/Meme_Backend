from rest_framework import serializers
from django.conf import settings
from .models import Post
from django.conf import settings

class MemeCreateserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','user','caption','URL','timestamp']
        
class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','user','caption','URL']