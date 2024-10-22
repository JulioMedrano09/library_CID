from django import forms
from .models import Book 


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, label="title")
    author = forms.CharField(max_length=100, label="author")
    category = forms.CharField(max_length=100, label="category")
    publish_date = forms.DateField(label="publish_date", required=False)
    editorial = forms.CharField(max_length=100, label="editorial")
    pages = forms.DecimalField(max_digits=10, decimal_places=0, label="pages")
    description = forms.CharField(max_length=500, label="description")
    files = forms.FileField(label="files", required=False)
    images = forms.ImageField(label="images", required=False)
    
    
    def save(self):
        Book.objects.create(
            title = self.cleaned_data['title'],
            author = self.cleaned_data['author'],
            category = self.cleaned_data['category'],
            publish_date = self.cleaned_data['publish_date'],
            editorial = self.cleaned_data['editorial'],
            pages = self.cleaned_data['pages'],
            description = self.cleaned_data['description'],
            files = self.cleaned_data['files'],
            images = self.cleaned_data['images'],
         )
         