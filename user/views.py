from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("sign_in")    
    else:
        form = forms.SignUpForm()

    return render(request, "user/sign_up.html", {"form": form})

