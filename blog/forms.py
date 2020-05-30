from django import forms
from .models import Comment, Category, Post 
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        exclude = ('slug',)
        widgets = {
            'content': SummernoteWidget(),
        }
