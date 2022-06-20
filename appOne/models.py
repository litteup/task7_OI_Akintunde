from django.db import models

# Create your models here.
class Hotelinfo(models.Model):

    occupant_first_name = models.CharField(max_length=50)
    occupant_last_name = models.CharField(max_length=50)
    occupant_occupation = models.CharField(max_length=50)
    occupant_email = models.EmailField(null=True, blank=True)
    room_number = models.CharField(max_length=20)
    amount_paid = models.FloatField()
    number_of_night = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
   

    def __str__(self):
        return f'{self.occupant_last_name} {self.room_number}'


'''
occupant_first_name 
occupant_last_name 
occupant_occupation
occupant_email 
room_number 
amount_paid 
number_of_night 
start_date
end_date


'''