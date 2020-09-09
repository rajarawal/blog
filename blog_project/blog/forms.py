from django import forms

class SendMailForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False ,widget =  forms.Textarea)

from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
