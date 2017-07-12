
from django import forms

class RSA1Form(forms.Form):
    N = forms.CharField(label='N')
    e1 = forms.CharField(label='e1')
    C1 = forms.CharField(label='C1')
    e2 = forms.CharField(label='e2')
    C2 = forms.CharField(label='C2')

class RSA2Form(forms.Form):
    N = forms.CharField(label='N')
    e = forms.CharField(label='e')
    m = forms.CharField(label='m')