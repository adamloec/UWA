from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import is_valid_path, reverse_lazy
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, LoginForm

# Home View
# Visible to all, registered users, etc.
def home(request):
    return render(request, 'home.html')

# Register View
# New user registration view.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('dashboard'))
    form = RegistrationForm()

    errors = form.errors.get_json_data()
    if errors:
        for field, field_errors in errors.items():
            for error in field_errors:
                form.add_error(field, error.get('message'))
    
    return render(request, 'registration.html', {'form': form})

# Login View
# Returning user login view.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('dashboard'))
            
            else:
                form.add_error(None, 'Incorrect username or password.')
    form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

# Dashboard View
# Dashboard view for registered users upon logging into the web application.
@login_required
def dashboard(request):
    if request.user.has_subscription:
        pass

    return render(request, 'dashboard.html')