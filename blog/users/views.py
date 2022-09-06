from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from blog_app.models import Article
from users.forms import ProfileEditForm
from users.models import User_profile
from users.forms import User_registration_form, UserEditForm
from django.contrib.auth.models import User

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}!! :D'}
                return redirect('/blog/list-article')

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Usuario o contraseña inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            User_profile.objects.create(
                user = User.objects.get(email=form.cleaned_data["email"])
            )
            return redirect('/users/login/')
        else:
            context = {'error':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)
    elif request.method == 'GET':
        form = User_registration_form()
    return render(request, 'users/register.html', {'form':form})

def logout_request(request):
    logout(request)
    return redirect('/users/login/')

def view_profile(request):
    if request.user.is_authenticated:
        usuario = request.user
        user_profile = User_profile.objects.get(user=usuario)
        if request.method == 'POST':
            form = UserEditForm(request.POST)
            form_profile = ProfileEditForm(request.POST, request.FILES)
            if form.is_valid() and form_profile.is_valid():
                usuario.email = form.cleaned_data['email']
                usuario.first_name = form.cleaned_data['first_name']
                usuario.last_name = form.cleaned_data['last_name']
                usuario.save()

                user_profile.description = form_profile.cleaned_data['description']
                user_profile.image = form_profile.cleaned_data['image']
                user_profile.save()
                return redirect('/users/profile/')
            else:
                context = {'error':form.errors}
                form = UserEditForm()
                context['formulario'] = form
                context['usuario'] = usuario
                return render(request, 'users/profile.html', context=context) 
        else:

            form = UserEditForm()
            form_profile = ProfileEditForm()
            context = {
                'usuario':usuario,
                'formulario_user':form,
                'formulario_profile': form_profile,
                'posts': len(Article.objects.filter(author=usuario))
            }
        return render(request, 'users/profile.html', context=context)