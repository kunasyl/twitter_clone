from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from tweet.forms import AddTweetForm
from tweet.models import Tweet
from userprofile.forms import LogInForm, RegistrationForm


def authenticateuser(request):
    if request.user.is_authenticated:
        return render(request, 'userprofile.html')
    else:
        if request.method == 'POST':
            if 'registrationform' in request.POST:
                registrationform = RegistrationForm(data=request.POST)
                loginform = LogInForm()

                if registrationform.is_valid():
                    username = registrationform.cleaned_data['username']
                    password = registrationform.cleaned_data['password1']
                    registrationform.save()
                    user = authenticate(username=username, password=password)
                    # LogIn user as soon as registered
                    login(request, user)
                    return redirect('/')
            else:
                loginform = LogInForm(data=request.POST)
                registrationform = RegistrationForm()

                if loginform.is_valid():
                    login(request, loginform.get_user())
                    return redirect('/')
        else:
            registrationform = RegistrationForm()
            loginform = LogInForm()

        return render(request, 'authentication.html', {'registrationform': registrationform, 'loginform': loginform})


def signout(request):
    logout(request)
    return redirect('/')


def alltweets(request):
    if request.user.is_authenticated:
        tweets = Tweet.objects.all()
        print("tweets are : ", tweets)
        return render(request, 'alltweets.html', {'tweets': tweets})


def timeline(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == 'POST':
            form = AddTweetForm(data=request.POST)

            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()

                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
        else:
            form = AddTweetForm()

        return render(request, 'userprofile.html', {'form': form, 'user': user})
    else:
        return redirect('/')
