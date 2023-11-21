from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm

# Create your views here.
# def say_hello(request):
#     return render(request, 'todo_list.html', {'name' : 'Gordon Ramsay', 'location' : 'UK'})

def gallery(request):
    return render(request, 'gallery.html',)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POst)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
