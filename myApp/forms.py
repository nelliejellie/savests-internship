from django import forms

class EmailPostForm(forms.Form):
    sender = forms.CharField(max_length=25)
    email_body = forms.CharField(required=False, widget=forms.Textarea)