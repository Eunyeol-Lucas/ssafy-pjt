from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, UserCreationForm
from django.contrib.auth import login
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)
