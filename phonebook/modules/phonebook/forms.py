from django import forms
from django.core.exceptions import ValidationError
from .models import ContactModel, PhoneNumbers


class AddContactForm(forms.ModelForm):
    phonenumber     = forms.CharField(max_length=255, min_length=10, label='Multi Numbers', widget=forms.TextInput(attrs={"class":"form-control", "aria-label":"phone number", 'placeholder':'Please use "," for multinumbers +966 ..., +966 ..., ...'}))

    class Meta:
        model   = ContactModel
        fields  = ['contact']
        widgets     = {'contact':forms.TextInput(attrs={"class":"form-control", "aria-label":"First Name", 'placeholder':'Sara Khoja'}),
                      }

    
    def clean(self):
        print(self.cleaned_data)
        '''Some validation before saving'''
        contact         = self.cleaned_data.get('contact')
        phonenumber     = self.cleaned_data.get('phonenumber')
        duplicated      = PhoneNumbers.objects.filter(phone=phonenumber)
        print('Duplicated is', duplicated)
        if not contact or contact == '' or ' ' not in contact:
            raise ValidationError('Please insert the good fullname same as Sara Khoja')
        elif not phonenumber or len(phonenumber)  != 13:
            raise ValidationError('Please insert the good phone number starts with +966')
        elif len(duplicated) > 0:
            raise ValidationError('The phonenumber is exist')
        if ',' in phonenumber:
            obj_len = phonenumber.split(',')
            if obj_len > 10:
                raise ValidationError('In Beta version we are only support 10 numbers for each user')
            

        return super().clean()
    

    def save(self, commit=True):
        obj         = super().save(commit=False)
        numbers     = self.cleaned_data.get('phonenumber').split(',')

        if commit:
            obj.save(commit)
        for number in numbers:
            number  = number.strip()
            if number:
                PhoneNumbers.objects.create(contact_id=obj, phone=number)
        return obj