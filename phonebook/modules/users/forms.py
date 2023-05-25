from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserModel

class UserLogin(AuthenticationForm):
    username    = forms.CharField(max_length=20, min_length=10, label='Phone Number', widget=forms.TextInput(attrs={"class":"form-control", "aria-label":"phone number", 'placeholder':'+966 5x xxx xxxx'}))
    password    = forms.CharField(max_length=15, label='password', widget=forms.PasswordInput(attrs={"class":"form-control", "aria-label":"email", 'placeholder':'*********'}))

class UserRegister(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control", "aria-label":"email", 'placeholder':'*********'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={"class":"form-control", "aria-label":"email", 'placeholder':'*********'}))

    class Meta:
        model       = UserModel
        fields      = ['firstname', 'lastname', 'phone', 'email']
        widgets     = {'firstname':forms.TextInput(attrs={"class":"form-control", "aria-label":"First Name", 'placeholder':'Ali'}),
                       'lastname':forms.TextInput(attrs={"class":"form-control", "aria-label":"Last Name", 'placeholder':'Elsayed'}),
                       'phone':forms.TextInput(attrs={"class":"form-control", "aria-label":"phone", 'placeholder':'+966 5x xxx xxxx'}),
                       'email':forms.EmailInput(attrs={"class":"form-control", "aria-label":"email", 'placeholder':'ali@pwc.com'})
                      }
        
        labels      = {'firstname':'First Name', 'lastname':'Last Name', 'phone':'Phone Number', 'email':'Email', 'password':'Password'}

        def clean_password2(self):
            # Check that the two password entries match
            password = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password and password2 and password != password2:
                raise ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control", "aria-label":"email", 'placeholder':'*********'}))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={"class":"form-control", "aria-label":"email", 'placeholder':'*********'}))
    class Meta:
        model       = UserModel
        fields      = ['firstname', 'lastname', 'phone', 'email']
        widgets     = {'password1':forms.PasswordInput, 
                       'password2':forms.PasswordInput,
                      }
        

        def clean_password2(self):
            # Check that the two password entries match
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user
        
class UserUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        fiedls = '__all__'