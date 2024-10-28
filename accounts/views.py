from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SubscriberForm, ContactForm
from blogposts.models import Article, Category

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Please login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('homepage')

# newsletter
def subscribe(request):
    articles = Article.objects.all().order_by("-published_date")
    categories = Category.objects.all()
    side_articles = Article.objects.all().order_by("-published_date")[:4]
    latest_articles = Article.objects.filter(is_latest=True).order_by("-published_date")[:5]
    entertainment_category = Category.objects.get( name="entertainment")
    technology_category = Category.objects.get(name="technology")
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully subscribed to our newsletter!")
            print("Success message added")
            return render(request, 'subscribe.html')  # Or another relevant page
    else:
        form = SubscriberForm()

    return render(request, 'index.html', {
        'form': form,
        'articles': articles,
        'latest_articles':latest_articles,
        'side_articles':side_articles,
        'entertainment_category':entertainment_category,
        'technology_category': technology_category,
        'categories':categories
        
        })

def contact(request):
    articles = Article.objects.all().order_by("-published_date")
    categories = Category.objects.all()
    side_articles = Article.objects.all().order_by("-published_date")[:4]
    latest_articles = Article.objects.filter(is_latest=True).order_by("-published_date")[:5]
    entertainment_category = Category.objects.get( name="entertainment")
    technology_category = Category.objects.get(name="technology")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!. We will get back in the shortest possible time")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'articles':articles,
        "categories":categories,
        "side_articles":side_articles,
        "latest_articles":latest_articles,
        "entertainment_category":entertainment_category,
        "technology_category":technology_category

        
        })


