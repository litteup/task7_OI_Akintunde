from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('home/', views.home, name = 'home'),
    path('booking/', views.booking, name = 'booking'),
    path('reservations/', views.reservations, name = 'reservations'),
    path('services/', views.services, name='services'),
    path('about/',views.about,name='about'),
    
]


#1. " " -- takes you to the default 'home' page
#2. localhost:8000/home takes you to the homepage
#3. /booking takes you to the booking page where management can enter the customer's details and request
#4. /reservations shows the reservations already make 
#5. /services shows other services XYZ Hotel provides
#6. /about talks about XYZ hotel