from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':                # ako je pokrenuta registracija
        form = UserRegisterForm(request.POST)   # spremi sve u form
        if form.is_valid():                     # provjeri spremljene podatke
            form.save()                         # ovo sprema podatke o useru, sve od username, lozinke, mail itd.
            username = form.cleaned_data.get('username')    # ako je sve ispravno, pokupi s forme upisani username
            messages.success(request, f'Account created for {username}!')   # javi poruku, f je fsting format
            return redirect('blog-home')        # redirect nas vraća na zadanu stranicu
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})