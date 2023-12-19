#from django.shortcuts import render
from .models import Article 
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.http import Http404 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.http import require_POST
from .forms import CommentForm
from taggit.models import Tag
# Create your views here.
def list_of_articles(request,tag_slug=None):
    articles=Article.publishedArticles.all()
    #print(artcles)
    paginator=Paginator(articles,3)
    page_number=request.GET.get('page',1)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags__in=[tag])
    try:
        articles=paginator.page(page_number)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        articles=paginator.page(1)

    return render (request ,'blog_app/list.html',{'articles':articles})
    pass


def article_details(request,year,month,day,article):
    try:
        article=get_object_or_404(Article, status=Article.Status.PUBLISHED,
                                  slug=article,
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day
                                  )
        comments=article.comments.filter(active=True)# List of active comments for this article
        # Form for users to write comment
        form = CommentForm()
    except Article.DoesNotExist:
        raise Http404("No Article Found")
    
    return render (request , 'blog_app/detail.html',{'article':article,'comments':comments,'form':form})
    pass

@require_POST
def comment_for_article(request, article_id):

    # get the article by article_id
    article = get_object_or_404(Article, id = article_id, status=Article.Status.PUBLISHED)
    comment = None
    
    # A comment form
    form = CommentForm(data=request.POST)

    if form.is_valid():
        # Create a Comment object before saving it to the database
        comment = form.save(commit=False)

        # Assign the article to the comment
        comment.article = article
        # Save the comment to the database
        comment.save()
        pass

    return render(request, 'blog_app/comment.html', {'article': article, 'form': form, 'comment': comment})

    pass

