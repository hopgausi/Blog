from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from .models import Article



class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publish']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Post Title'}),
            'content': Textarea(attrs={'placeholder': 'Post Content', 'cols':100, 'rows':100}),
        }
        labels = {
            'title': '',
            'content': '',
        }
        

