from django.shortcuts import render,redirect
from .forms import ResisterForm,ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def resister(request):
    if request.method == 'POST':
        register_form = ResisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect(resister)
    
    else:
        register_form = ResisterForm()
    return render(request, 'signup.html', {'form' : register_form, 'type' : 'Register'})
    



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                messages.success(request,'Logged in Successfully')
                login(request, user)
                return redirect('profile')  
            
    else:
        form = AuthenticationForm()
        return render(request, 'signup.html', {'form': form, 'type': 'Login'})
    

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})
def without_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request, 'Password Updated Successfully')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'pass_change.html', {'form': form})
    else:
        return redirect('login')
def user_logout(request):
    logout(request)
    return redirect(user_login)
