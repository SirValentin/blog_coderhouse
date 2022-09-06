from django import forms
from blog_app.models import Advertising

class FormArticle(forms.Form):
    title = forms.CharField(max_length=40)
    content = forms.CharField(max_length=200)
    image = forms.ImageField(required=False)

class FormAd(forms.Form):
    company = forms.CharField(max_length=20)
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)

    class Meta:
        model = Advertising
        fields = ('company', 'title', 'description', 'image')
        help_texts = {k:'' for k in fields}

class FormComent(forms.Form):
    text = forms.CharField(max_length=100)
    class Meta:
        model = Advertising
        fields = ('text')
        help_texts = {k:'' for k in fields}
