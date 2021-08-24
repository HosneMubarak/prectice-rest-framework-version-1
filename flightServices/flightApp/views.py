from django.shortcuts import render
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def find_flights(request):
    flight = Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'],
                                   dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(flight, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    passenger.save()

    reservation = Reservation()
    serializer = ReservationSerializer(reservation)

    reservation.passenger = passenger
    reservation.flight = flight

    reservation.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
