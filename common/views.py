
from django.contrib import auth


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from common.forms import UserForm


#로그인 구현
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'common/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'common/login.html')

#로그아웃 구현
def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
