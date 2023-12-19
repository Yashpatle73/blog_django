from django import template
from ..models import Article
from django.db.models import Count


register =template.Library()


@register.simple_tag
def total_articles():
    return Article.publishedArticles.count()
    pass


@register.inclusion_tag('blog_app/latest_articles.html')
def show_latest_articles(count=3):
    latest_articles = Article.publishedArticles.order_by('-publish')[:count]
    return {'latest_articles': latest_articles}
    pass


@register.inclusion_tag('blog_app/most_commented_articles.html')
def show_most_commented_articles(count=3):
    most_commented_articles = Article.publishedArticles.annotate(
                                    total_comments=Count('comments')
                                ).order_by('-total_comments')[:count]
                                
    return {'most_commented_articles' : most_commented_articles}
    pass