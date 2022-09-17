from django.shortcuts import render
from news.models import articles
from forms import ArticleCreateForm

# Create your views here.
def create_news(request):
    if request.method == 'POST':
        pass
    else:
        form = ArticleCreateForm()
    return render(request, '')
