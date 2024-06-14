from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.contrib import messages


def home(request):
    return render(request, 'base.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            birth_day = form.cleaned_data.get('birth_day')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            address = form.cleaned_data.get('address')

            user = CustomUser.objects.create_user(
                full_name=full_name,
                birth_day=birth_day,
                phone=phone,
                gender=gender,
                address=address,
            )
            login(request, user)
            return redirect('success')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_admin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data['phone']

            try:
                user = CustomUser.objects.get(full_name=full_name, phone=phone)  # Assuming phone is password
                if user is not None and user.full_name == full_name:
                    login(request, user)
                    return redirect('table-users')
                else:
                    form.add_error(None, 'Invalid credentials')
            except ObjectDoesNotExist:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def success(request):
    user = request.user
    return render(request, 'success.html', {'user': user.full_name})


def handling_404(request, exception):
    return render(request, '404.html', {})


def handling_500(request):
    return render(request, '500.html')


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


def table_user(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Sizga bu sahifani ko'rish huquqi berilmagan.")
    users = CustomUser.objects.filter(is_staff=False)
    return render(request, 'table_user.html', {'users': users})


def delete_user(request, user_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Sizga bu sahifani ko'rish huquqi berilmagan.")

    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, f"Foydalanuvchi {user.full_name} muvaffaqiyatli o'chirildi.")

    return HttpResponseRedirect(reverse('table-users'))