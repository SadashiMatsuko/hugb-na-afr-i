from django.forms import ModelForm, widgets
from models import articles


class ArticleCreateForm(ModelForm):
    class Meta:
        model = articles
        exclude = ['id']
        widgets = {
            'title': widgets.TextInput, 'text': widgets.Textarea, 'date_posted': widgets.DateTimeInput
        }
