from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from webrepetitor.sitemaps import BdSitemap

sitemaps = {'posts': BdSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webrepetitor.urls')),
    path('webrepetitor/', include('webrepetitor.urls', namespace='webrepetitor')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')


]
