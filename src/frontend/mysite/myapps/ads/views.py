# -*- coding utf-8 -*- #
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from myapps.ads.models import Category

from myapps.ads.models import Food
from schedule.periods import Week


def list(request):
    return render(request, 'ads/list.html', {'test': 'gniaaa'})

def category(request, category=None):

    if category:
        categorie = get_object_or_404(Category, slug=category)
        foods = Food.objects.filter(category=categorie)
        current_categorie = Category.objects.get(slug=category)
    else:
        foods = Food.objects.all()
        current_categorie = None

    categories = Category.objects.all()

    events = Week(foods, datetime.datetime(2008, 4, 1))

    paginator = Paginator(foods, 10) # Show 25 objects per page

    page = request.GET.get('page')
    try:
        page_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_objects = paginator.page(paginator.num_pages)

    return render(request, 'ads/meals.html', {'foods': page_objects,
                                            'categories': categories,
                                            'current_categorie': current_categorie,
                                            'events': events})