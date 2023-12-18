from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):

    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','published'

    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_articles")
    title=models.CharField(max_length=300)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),]

    def __str__(self) -> str:
        return self.title
        pass
    
    pass
    
    
