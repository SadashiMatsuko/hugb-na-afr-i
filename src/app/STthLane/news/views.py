from django.shortcuts import render, get_object_or_404, redirect
from news.models import articles
from news.forms import ArticleCreateForm


# Create your views here.
def create_article(request):
    """ Creates a new article"""
    if request.method == 'POST':
        article_form = ArticleCreateForm(data=request.POST)
        if article_form.is_valid():
            articles = article_form.save()
            return redirect('/')
    else:
        article_form = ArticleCreateForm()
    return render(request, 'news/create_article.html', {
        'article_form': article_form
    })
