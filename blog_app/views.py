#from django.shortcuts import render
from .models import Article 
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.http import Http404
# Create your views here.
def list_of_articles(request):
    articles=Article.publishedArticles.all()
    #print(artcles)

    return render (request ,'blog_app/list.html',{'articles':articles})
    pass


def article_details(request,id):
    try:
        article=get_object_or_404(Article,id=id , status=Article.Status.PUBLISHED)
    except Article.DoesNotExist:
        raise Http404("No Article Found")
    
    return render (request , 'blog_app/detail.html',{'article':article})
    pass



