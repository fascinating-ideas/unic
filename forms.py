from django import forms  
from application.models import user,book,contact   
class UserForm(forms.ModelForm):  
    class Meta:  
        model = user  
        fields = "__all__" 
class bookForm(forms.ModelForm):  
    class Meta:  
        model = book  
        fields = "__all__" 
class contactForm(forms.ModelForm):  
    class Meta:  
        model = contact  
        fields = "__all__"                  