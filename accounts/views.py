from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm, UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.forms import (
    EditProfileForm
)


# Create your views here.


def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # Added username after video because of error returning customer name if not added
            Customer.objects.create(
                user=user,
                name=user.username,
            )
            messages.success(request, 'Un compte a été créé pour ' + username)
            return redirect("accounts:login_url")

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_url(request):
    if request.method == 'Post':
        username = request.Post.get('username')
        password = request.Post.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('accounts:view_profile'))
        else:
            messages.info(request, 'identifiant ou le mot de passe est incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_url')


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request, 'registration/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        messages.success(request, 'votre mot de passe a été modifié.')
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change_password.html', args)


def edit_all(request):
    title = "custmize Profile"
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfile(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("accounts:view_profile")
    else:
        form = UserProfile(instance=userProfile)
    return render(request, 'registration/editall.html', {'title': title, "form": form})


def delete_profile(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    messages.success(request, 'Profile successfully disabled.')
    return redirect("accounts:login_url")


def activer_profile(request):
    logout(request)
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request, 'Profile successfully disabled.')
    return redirect("accounts:view_profile")




def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["nom"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['benabdallah65emna@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'registration/contact.html', {'form': form})
