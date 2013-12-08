from django.views.generic import TemplateView

from .models import Article


# Create your views here.
class BlogView(TemplateView):
    template_name = 'blog/blog_index.html'

    def get(self, request, **kwargs):
        context = self.get_context_data()
        context['articles'] = Article.objects.all()

        return self.render_to_response(context)


class ArticleView(TemplateView):
    template_name = ''

    def get(self, request, **kwargs):
        context = self.get_context_data()

        article = Article.objects.get(url_slug=kwargs.get('article_slug'))

        context['article'] = article

        self.template_name = article.template_name
        return self.render_to_response(context)
