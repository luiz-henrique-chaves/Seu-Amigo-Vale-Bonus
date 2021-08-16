from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from accounts import forms

user_active = ''


def registerPage(request):
	global user_active
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = forms.CreateUserForm()		

		if request.method == 'POST':
			form = forms.CreateUserForm(request.POST)
			if form.is_valid():
				account = form.save()
				name_user = form.cleaned_data.get('username')
				#user_id = account.pk				
				messages.success(request, 'A conta "' + name_user + '" foi criada com sucessso!')
				return redirect('login')			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginAPI(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)			
			if user is not None:
				user_active = user
				login(request, user)

				from aluno.models import Aluno 				
				if Aluno.objects.filter(id_usuario=user_active):
					return redirect('home')
				else:
					return redirect('create_aluno', profile=user_active)
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/loginAPI.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)			
			if user is not None:
				user_active = user
				login(request, user)

				from aluno.models import Aluno 				
				if Aluno.objects.filter(id_usuario=user_active):
					return redirect('home')
				else:
					return redirect('create_aluno', profile=user_active)
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')