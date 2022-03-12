from django.shortcuts import render
from cars.models import Car

from pages.models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(
        is_featured=True)
    all_cars=Car.objects.order_by('-created_date')
    # search_fields=Car.objects.order_by('model','year','city','state','body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars':all_cars,
        # 'search_fields':search_fields,
        'model_search':model_search,
        'year_search': year_search,
        'state_search':state_search,
        'body_style_search':body_style_search,

    }
    return render(request, "pages/index.html", data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
