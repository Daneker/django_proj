from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'surname', 'email', 'id']


    def clean(self): 
  
        # data from the form is fetched using super function 
        super(HomeForm, self).clean() 
          
        # extract the username and text field from the data 
        name = self.cleaned_data.get('name') 
        surname = self.cleaned_data.get('surname') 
        email = self.cleaned_data.get('email') 
        id = self.cleaned_data.get('id') 
  
        # conditions to be met for the username length 
        if len(name) < 5: 
            self._errors['name'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(surname) < 5: 
            self._errors['surname'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(email) < 5: 
            self._errors['email'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(id) != 9: 
            self._errors['id'] = self.error_class([ 
                '9 digits required']) 
  
        # return any errors if found 
        return self.cleaned_data 