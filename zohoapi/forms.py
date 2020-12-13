from django import forms

class TicketPostForm(forms.Form):
    department = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    priority = forms.IntegerField()