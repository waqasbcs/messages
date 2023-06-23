from django import forms
from . models import user
 
class studentregistration(forms.ModelForm):
     
     class Meta:
         model = user
         fields = ("name","password","email")