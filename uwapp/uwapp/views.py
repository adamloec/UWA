from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth import login, logout, authenticate

from .forms import RegistrationForm, LoginForm

# Home View
# Visible to all, registered users, etc.
def homeView(request):
    return render(request, 'home.html')

# Register View
# New user registration view.
def registrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('home'))
    else:
        form = RegistrationForm()
    
    error = None
    if form.errors:
        error = list(form.errors.as_data().values())[0][0].messages if form.errors else None
        error = str(', '.join(error)).replace('[','').replace(']','').replace('\'','')
    
    return render(request, 'registration.html', {'form': form, 'error': error})

# Login View
# Registered user login view.
def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))
    else:
        form = LoginForm()

    error = None
    if form.errors:
        error = list(form.errors.as_data().values())[0][0].messages if form.errors else None
        error = str(', '.join(error)).replace('[','').replace(']','').replace('\'','')

    return render(request, 'login.html', {'form': form, 'error': error})

# Logout View
#
def logoutView(request):
    logout(request)
    return redirect('home')

# Dashboard View
# Dashboard view for registered users upon logging into the web application.
@login_required
def dashboardView(request):
    if request.user.has_subscription:
        pass

    return render(request, 'dashboard/dashboard.html')