from django import forms



class EmailForm(forms.Form):
    email = forms.CharField(label='Электронная почта', max_length=200)
