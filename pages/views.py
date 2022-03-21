from unicodedata import name
from django.shortcuts import redirect, render
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from pages.models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(
        is_featured=True)
    all_cars=Car.objects.order_by('-created_date')
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
    if request.method== "POST":
        name=request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        message_body= 'Name:- ' + name + ' email:- ' + email + ' phone:- ' + phone + ' message:-' + message
        email_subject='you have a new message regarding ' + subject
        admin_info = User.objects.get(is_superuser=True)
        admin_email=admin_info.email
        send_mail(
            email_subject,
            message_body,
            'stalonfernandes@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        return redirect('contact')

    return render(request, 'pages/contact.html')
