from ast import keyword
from django.shortcuts import get_object_or_404, render

from cars.models import Car
from . import views
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator= Paginator(cars,3)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    all_cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',
                                                flat=True).distinct()
    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'all_cars': all_cars,
        'year_search': year_search,
        'state_search': state_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html',data)


def car_detail(request,id):
    single_car= get_object_or_404(Car, pk=id)

    data={
        'single_car':single_car,
    }

    return render(request,'cars/car_detail.html',data)


def search(request):
    cars= Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',
                                                flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission',
                                                    flat=True).distinct()

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)


    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model__iexact=model)


    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            cars=cars.filter(state__iexact=state)


    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)


    if 'body_style' in request.GET:
        body_style=request.GET['body_style']
        if body_style:
            cars=cars.filter(body_style__iexact=body_style)


    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)



    data = {
        'model_search': model_search,
        'year_search': year_search,
        'state_search': state_search,
        'body_style_search': body_style_search,
        'transmission_search':transmission_search,
        'cars': cars
    }
    return render(request,'cars/search.html',data)