from django import forms
from .models import Post, Comment
class CommentForm(forms.Form):
 
    body = forms.CharField(widget= forms.Textarea(
        attrs= {
            "class": "form-control",
            "placeholder": "Leave a Comment: "
        }
    ))
