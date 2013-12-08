from django.conf.urls import patterns, url

from .views import BlogView, ArticleView


urlpatterns = patterns(
    '',
    url(r'^$', BlogView.as_view(), name='blog'),
    url(r'^article/(?P<article_slug>[\w-]+)$', ArticleView.as_view(), name='article')
)
