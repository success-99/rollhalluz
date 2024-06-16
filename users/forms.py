from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser


class LoginForm(forms.Form):
    full_name = forms.CharField(label='Ism', max_length=255)
    phone = forms.CharField(max_length=9, label='Parol')


def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError("Telefon nomer raqamlardan iborat bo'lsin.")


def validate_string(value):
    if not value.isalpha():
        raise ValidationError("Familiya va Ismingiz harflardan iborat bo'lsin.")


class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=255, required=True, validators=[validate_string])
    birth_day = forms.IntegerField(min_value=7, max_value=15)
    phone = forms.CharField(min_length=9, max_length=9, required=True, validators=[validate_numeric], error_messages={
        'min_length': 'Telefon raqam kamida 9 ta belgidan iboratligiga ishonch hosil qiling.',
        'max_length': 'Telefon raqam ko‘pi bilan 9 ta belgidan iboratligiga ishonch hosil qiling.',
        'required': 'Ushbu maydon to‘ldirilishi shart.',
        'invalid': 'Telefon raqam faqat raqamlardan iborat bo‘lishi kerak.'
    })
    address = forms.CharField(max_length=255, required=True)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Bunday nomer egasi mavjud.")
        return phone

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if CustomUser.objects.filter(full_name=full_name).exists():
            raise forms.ValidationError("Bunday Ismli foydalanuvchi egasi mavjud.")
        return full_name


class SignupForm1(forms.Form):
    full_name = forms.CharField(max_length=255, required=True, validators=[validate_string])
    birth_day = forms.IntegerField(min_value=16, max_value=70)
    phone = forms.CharField(min_length=9, max_length=9, required=True, validators=[validate_numeric], error_messages={
        'min_length': 'Telefon raqam kamida 9 ta belgidan iboratligiga ishonch hosil qiling.',
        'max_length': 'Telefon raqam ko‘pi bilan 9 ta belgidan iboratligiga ishonch hosil qiling.',
        'required': 'Ushbu maydon to‘ldirilishi shart.',
        'invalid': 'Telefon raqam faqat raqamlardan iborat bo‘lishi kerak.'
    })
    address = forms.CharField(max_length=255)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Bunday nomer egasi mavjud.")
        return phone

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if CustomUser.objects.filter(full_name=full_name).exists():
            raise forms.ValidationError("Bunday Ismli foydalanuvchi egasi mavjud.")
        return full_name
