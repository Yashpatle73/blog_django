from django.contrib.sitemaps import Sitemap
from .models import Article

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Article.publishedArticles.all()
        pass

    def lastmod(self, obj):
        return obj.updated
        pass
    pass
