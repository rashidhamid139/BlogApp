from django import forms
from .models import Post, Comment
class CommentForm(forms.ModelForm):
 
    body = forms.CharField(widget= forms.Textarea(
        attrs= {
            "class": "form-control",
            "placeholder": "Leave a Comment: "
        }
    ))
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('author', )
