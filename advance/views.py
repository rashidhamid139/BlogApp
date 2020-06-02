from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import csv
# Create your views here.
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]

def unruly_passengers_csv(request):
    response = HttpResponse("text/csv")
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])

    return response

