from .models import Flight, Passenger, Reservation
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flightNumber(self, flightNumber):
        if flightNumber == '123456':
            raise serializers.ValidationError("Not match 123456")
        return flightNumber


class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
