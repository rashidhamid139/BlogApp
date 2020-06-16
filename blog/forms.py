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



class FeedBackForm(forms.Form):
    name = forms.CharField(widget = forms.Textarea(
        attrs={
            "type": "text",
            "placeholder": "Name"
        }
    ))
    email = forms.EmailField(widget = forms.Textarea(
        attrs={
            "placeholder": "E-Mail"
        }
    ))
    subject = forms.CharField(widget = forms.Textarea(
        attrs={
            "placeholder": "Subject"
        }
    ))
    message = forms.CharField(widget = forms.Textarea(
        attrs={
            "placeholder": "Message"
        }
    ))


