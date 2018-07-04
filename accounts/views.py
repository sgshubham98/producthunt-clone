from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['confirmpassword']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'*Username has been already taken!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password'], email=request.POST['email'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'accounts/signup.html', {'error':'*Password doesn\'t match '})		
	else:
		return render(request, 'accounts/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error':'*Username/Password is Incorrect.'})
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')