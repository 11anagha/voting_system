from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import logout

def sign_up(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        
        if form.is_valid():
            age = form.cleaned_data.get("age")
            
            if age <= 18:
                messages.error(request, "You must be at least 18 years old to be eligible to vote.")
                return redirect("sign_up")
            else:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect("sign_in")    
    else:
        form = forms.SignUpForm()

    return render(request, "user/sign_up.html", {"form": form})



def sign_out(request):
    logout(request)
    return render(request, "user/sign_out.html")