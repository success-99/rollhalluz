from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    full_name = forms.CharField(label='Ism', max_length=255)
    phone = forms.CharField(max_length=9, label='Parol')


class SignupForm(forms.Form):

    GENDER_CHOICES = [
        ("F", "o'g'il bola"),
        ("M", 'qiz bola'),
    ]

    full_name = forms.CharField(max_length=255, required=True)
    birth_day = forms.IntegerField(min_value=7, max_value=15)
    phone = forms.CharField(max_length=9, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    address = forms.CharField(max_length=255, required=True)


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A user with that phone number already exists.")
        return phone

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if CustomUser.objects.filter(full_name=full_name).exists():
            raise forms.ValidationError("A user with that full name already exists.")
        return full_name

