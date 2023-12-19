from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class ArticlePublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Article.Status.PUBLISHED)
        pass
    pass


class Article(models.Model):

    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','published'

    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_articles")
    title=models.CharField(max_length=300)
    slug=models.SlugField(max_length=250 , unique_for_date='publish')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    objects=models.Manager()#The default manager
    publishedArticles=ArticlePublishedManager()#the custom manager
    tags=TaggableManager()
    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),]

    def __str__(self) -> str:
        return self.title
        pass
    

    def get_absolute_url(self):
        return reverse("blog_app:article_details" , args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug])

    pass
    
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    class Meta:
        ordering=['created']
        indexes=[
            models.Index(fields=['created']),
        ]   
    def __str__(self) -> str:
        return f'Comment by {self.name} on {self.article}'
        pass
    
    pass
