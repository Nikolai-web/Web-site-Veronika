from .models import Bd
from django.contrib.sitemaps import Sitemap

class BdSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Bd.published.all()

    def lastmod(self, obj):
        return obj.updated
