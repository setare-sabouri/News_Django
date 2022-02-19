import imp
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from matplotlib.style import use


def signup_user(request):
    if request.method == 'POST':    #send data from client to server
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.is_teacher = True
            user.is_staff = True

            #login(request,user)
            #login
            user.save()

            return redirect('News:home')
    else:                                  # data from server to clinet (template to sugn up)
        form = UserCreationForm()                  
    return render(request,'signUp.html',{'form':form})




def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login user
            user = form.get_user()

            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('News:list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)

        return redirect('News:list')


