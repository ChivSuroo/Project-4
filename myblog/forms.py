from django import forms
from .models import Post, Category

#choices = [('pc', 'PC'), ('playstation', 'Playstation'), ('xbox', 'Xbox'),]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Here...'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag Here...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Here...'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Here...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag Here...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Here...'}),
        }
