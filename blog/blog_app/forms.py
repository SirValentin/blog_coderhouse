from django import forms

class FormArticle(forms.Form):
    title = forms.CharField(max_length=40)
    content = forms.CharField(max_length=200)
    author = forms.CharField(max_length=30)

class FormAuthor(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=40)
    description = forms.CharField(max_length=100)

class FormAd(forms.Form):
    company = forms.CharField(max_length=20)
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100)