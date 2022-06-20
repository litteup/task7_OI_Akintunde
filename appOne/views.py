from django.shortcuts import render,redirect
from . forms import BookingForm
from . models import Hotelinfo
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request,'appOne/base.html')

def about(request):
    return render(request,'appOne/about.html')

def services(request):
    return render(request,'appOne/services.html')

def home(request): #renders homepage - index
    return render (request,'appOne/home.html')

def reservations(request):
    booked_rooms = Hotelinfo.objects.all()
    return render(request,'appOne/reservations.html',{'booked_rooms':booked_rooms})


def booking(request):
    if request.method == 'POST':
        occupant_first_name = request.POST['occupant_first_name']
        occupant_last_name = request.POST['occupant_last_name']
        occupant_occupation = request.POST['occupant_occupation']
        occupant_email = request.POST['occupant_email']
        room_number = request.POST['room_number']
        amount_paid = request.POST['amount_paid']
        number_of_night = request.POST['number_of_night']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        instance = Hotelinfo(occupant_first_name=occupant_first_name,
                            occupant_last_name=occupant_last_name,
                            occupant_occupation=occupant_occupation,
                            occupant_email=occupant_email,
                            room_number=room_number,
                            amount_paid=amount_paid,
                            number_of_night=number_of_night,
                            start_date=start_date,
                            end_date=end_date)
        instance.save()
        messages.success(request,("New Booking Added Successfully"))
        return redirect(home)

    return render(request,'appOne/makeBooking.html')





"""
def booking(request): #renders booking page
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,("New Booking Added Successfully"))
        return redirect(home)
    return render (request, 'appOne/makeBooking.html',{'form':form})


"""

'''
def booking_view(request): # creates models into form
    form = BookingForm()
    return render(request, "appOne/makeBooking.html", {'form':form})
'''
'''
def savebooking(request):
    form = BookingForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        print('Booking Successful!')

    return render(request,'appOne/home.html',{'form':form})

'''

'''
def booking_view(request): # creates models into form
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print('Form is valid!')
            print( 'First Name',form.cleaned_data['occupant_first_name'])
            print('Last Name', form.cleaned_data['occupant_last_name'])
            print('Email', form.cleaned_data['occupant_email'])
            print('Room Number', form.cleaned_data['room_number'])
            print('Amount Paid', form.cleaned_data['amount_paid'])
            print('Number of Night', form.cleaned_data['number_of_night'])
            print('Start Date', form.cleaned_data['start_date'])
            print( 'End Date', form.cleaned_data['end_date'])
            print('Comment', form.cleaned_data['comment'])


    return render(request, "appOne/makeBooking.html", {'form':form})

'''

"""
def sendToDb_1(request):
    if request.method == 'POST':
        bc = BookingForm(request.POST)
        if bc.is_valid():
            occupant_first_name = bc.cleaned_data['occupant_first_name']
            occupant_last_name = bc.cleaned_data['occupant_last_name']
            occupant_email = bc.cleaned_data['occupant_email']
            room_number = bc.cleaned_data['room_number']
            amount_paid = bc.cleaned_data['amount_paid']
            number_of_night = bc.cleaned_data['number_of_night']
            start_date = bc.cleaned_data['start_date']
            end_date = bc.cleaned_data['end_date']
            comment = bc.cleaned_data['comment']
            booking = Hotelinfo(
            occupant_first_name = occupant_first_name,
            occupant_last_name = occupant_last_name,
            occupant_email = occupant_email,
            room_number = room_number,
            amount_paid = amount_paid,
            number_of_night = number_of_night,
            start_date = start_date,
            end_date = end_date,
            comment = comment
            )
            booking.save()
            messages.success(request,'Booking Successful!')
    else:
        bc = BookingForm()
    return render (request,'appOne/home.html',{'form':bc})


"""









'''
def sendToDb_1(request):
    if request.method == 'POST':
        occupant_first_name = request.POST['occupant_first_name']
        occupant_last_name = request.POST['occupant_last_name']
        occupant_email = request.POST['occupant_email']
        room_number = request.POST['room_number']
        amount_paid = request.POST['amount_paid']
        number_of_night = request.POST['number_of_night']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        comment = request.POST['comment']
        booking = Hotelinfo.objects.create(
            occupant_first_name = occupant_first_name,
            occupant_last_name = occupant_last_name,
            occupant_email = occupant_email,
            room_number = room_number,
            amount_paid = amount_paid,
            number_of_night = number_of_night,
            start_date = start_date,
            end_date = end_date,
            comment = comment
            )
        messages.success(request,'Booking Successful!')
        return render (request,'appOne/home.html')

'''
'''
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('Booking Successful!')

    return render(request,'appOne/home.html',{'form':form})
'''