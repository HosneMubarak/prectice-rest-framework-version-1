from django.db import models


# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    arrivalCity = models.CharField(max_length=20)
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return f"{self.flightNumber} - {self.operatingAirlines} - {self.departureCity} to {self.arrivalCity}"


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger.firstName} {self.passenger.lastName} Flight {self.flight.operatingAirlines} {self.flight.flightNumber}"
