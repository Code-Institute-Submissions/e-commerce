from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_index(request):
    return render(request, "accounts/index.html")
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have sucessfully logged out")
    return redirect("home")


def login(request):
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                messages.success(request, "You have sucessfully logged in")
                if request.GET and 'next' in request.GET:
                	next = request.GET['next']
                	return redirect(next)
                else:
                	return redirect('home')
                return redirect("home")
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
        
    else:
        form = UserLoginForm()
    
    
    return render(request, 'accounts/login.html', { 'form': form })
    
def profile(request):
    return render(request, 'accounts/profile.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form}) 
    

 