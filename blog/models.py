from django.db import models

# Create your models here.

class Post(models.Model): #일종의 DB구조,field 설정
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField()