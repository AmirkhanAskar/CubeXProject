
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.contrib import messages

from .models import Blog
from .forms import BlogForm


def home(request):
    return render(request, 'cubexmain/home.html')


def about(request):
    return render(request, 'cubexmain/about.html')


def pricing(request):
    return render(request, 'cubexmain/pricing.html')


def features(request):
    return render(request, 'cubexmain/features.html')


def blog(request):
    return render(request, 'cubexmain/blog.html')


def eachblog(request):
    return render(request, 'cubexmain/eachBlog.html')


def blogarticle(request):
    return render(request, 'cubexmain/blogArticle.html')


def integration(request):
    return render(request, 'cubexmain/integration.html')


def account_login(request):
    return render(request, 'cubexmain/account.html')


def account_register(request):
    return render(request, 'cubexmain/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Редирект на страницу home после успешной аутентификации
    return render(request, 'cubexmain/account.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')  # Редирект на главную страницу после выхода пользователя


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Проверка, что пароли совпадают
        if password1 == password2:
            # Проверка, что пользователя с таким именем еще не существует
            if not User.objects.filter(username=username).exists():
                # Создание нового пользователя
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
            else:
                messages.error(request, 'Username is already taken.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'cubexmain/register.html')


def profile(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user  # Привязываем блог к текущему пользователю
            blog.save()
            return redirect('profile')  # Перенаправляем пользователя обратно на страницу кабинета после сохранения блога

    else:
        blog_form = BlogForm()

    context = {
        'blog_form': blog_form,
    }
    return render(request, 'profile.html', context)