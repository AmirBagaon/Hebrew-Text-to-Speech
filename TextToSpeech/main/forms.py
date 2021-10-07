from django import forms
   
# creating a form 
class InputForm(forms.Form):
   
    
    first_name = forms.CharField()

class TranslateForm(forms.Form):
    placeholder = forms.CharField()

