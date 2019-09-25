from django import forms


class ContactsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label='E-mail')
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)
