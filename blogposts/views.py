from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Q
from .models import Article, Category, Banner
from itertools import chain

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by("-published_date")
    categories = Category.objects.all()
    side_articles = Article.objects.all().order_by("-published_date")[:4]
    latest_articles = Article.objects.filter(is_latest=True).order_by("-published_date")[:5]
    entertainment_category = Category.objects.get( name="entertainment")
    technology_category = Category.objects.get(name="technology")
    advert_top = Banner.objects.filter(is_home_banner_top=True).order_by("-updated_date")[:1]
    advert_center = Banner.objects.filter(is_home_banner_center=True).order_by("-updated_date")[:1]
    advert_bottom = Banner.objects.filter(is_home_banner_bottom=True).order_by("-updated_date")[:1]

    return render(request, 'index.html', {
        'articles': articles,
        'latest_articles':latest_articles,
        'side_articles':side_articles,
        'entertainment_category':entertainment_category,
        'technology_category': technology_category,
        'categories':categories,
        "advert_top":advert_top,
        "advert_center":advert_center,
        "advert_bottom":advert_bottom,
    })

def blog_item(request, pk=None): 
    categories = Category.objects.all()
    articles = Article.objects.all().order_by("-published_date")
    if pk: 
        blog_item = Article.objects.get(pk=pk) 
    else: 
        blog_item = "" 
    return render(request, 'blog_item.html', {
        "blog_item": blog_item,
        "articles":articles,
        "categories":categories,
        
        }) 


def category_page(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    articles = category.articles.all()
    latest_articles = Article.objects.filter(is_latest=True).order_by("-published_date")[:5]
    advert = Banner.objects.filter(is_category_banner=True)
    return render(request, 'category_page.html', {
        "category":category, 
        "articles":articles,
        "latest_articles":latest_articles,
        "categories": categories,
        "advert":advert,
        
        })

def search(request):
    categories = Category.objects.all()
    articles = Article.objects.all().order_by("-published_date")
    query = request.GET.get('q')  # Get the search term from the query string
    results = None
    if query:
        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(content__icontains=query)
    
    context = {
        'results': results,
        'query': query,
        "categories":categories,
        "articles":articles,
        
    }
    return render(request, 'search.html', context)

def adverts(request):
    advert = Banner.objects.all()
    # advert = Banner.objects.filter(is_home_banner=True)
    return render(request, 'adverts.html', {
        "advert":advert,
    } )