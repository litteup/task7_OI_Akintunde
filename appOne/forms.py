from django import forms
from . models import Hotelinfo


class BookingForm(forms.ModelForm):
    #This prints all the columns in models to form
    class Meta:
        model = Hotelinfo
        fields = '__all__'