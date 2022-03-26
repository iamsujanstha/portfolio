from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    content = forms.CharField(max_length = 1000, widget=forms.Textarea(attrs={'placeholder':'Body'}))