from django.shortcuts import render,redirect
from carsapp.forms import UserForm
from django.contrib.auth import login

# Create your views here.

def homepage(request):
    return render(request,'base.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
             
             
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:

                form.add_error('password2', 'Şifreler eşleşmiyor.')
                return render(request, 'registration/sign_up.html', {'form': form})
           
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Şifreyi hashle

            # Kullanıcıyı kaydet
            user.save()

            # Kullanıcıyı giriş yapmış olarak işaretle
            login(request, user)

            return render(request,'base.html')
        
    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})
    