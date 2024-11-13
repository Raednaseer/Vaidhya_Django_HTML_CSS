import re, datetime
from statistics import mode
from xml.parsers.expat import model
from django import forms
from .models import Consultation,User

class ConsultaionForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name:
            if not re.match(r'^[a-zA-Z\s]+$', name):
                raise forms.ValidationError("Only letters are allowed.")
            if len(name) < 4:
                raise forms.ValidationError("Length of name should be more than 4 characters.")
        
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?\d{10,15}$',phone):
            raise forms.ValidationError("Enter a valid phone number")

        return phone

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 3:
            raise forms.ValidationError("Enter you concern in detail")
        return message

    def clean(self):
        cleaned_data = super().clean()
        preferred_time = cleaned_data.get("preferred_time")
        preferred_date = cleaned_data.get("preferred_date")

        if preferred_time and (preferred_time < datetime.time(9) or preferred_time > datetime.time(17)):
            raise forms.ValidationError("Preferred time must be between 9 AM and 5 PM.")


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name:
            if not re.match(r'^[a-zA-Z\s]+$', name):
                raise forms.ValidationError("Only letters are allowed.")
            if len(name) < 4:
                raise forms.ValidationError("Length of name should be more than 4 characters.")
        return name

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password length should be minimum of 8")
        return password


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

        
    