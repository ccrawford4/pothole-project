from django.shortcuts import render
from django.http import HttpResponse
from .models import Report, Unit
import requests
import os
import pygeodesic.geodesic as geodesic

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, World! TEST Is this workflow actually working")

def home_page(request):
    report_data = Report.objects.all()
    unit_data = Unit.objects.all()
    context = {
        'report_data': report_data,
        'unit_data': unit_data,
    }
    return render(request, 'index.html', context=context)

def sort_report_data(report_data):
    return sorted(report_data, key=lambda x: x.Date)
    
def sort_unit_data(unit_data):
    return sorted(unit_data, key=lambda x: x.severity, reverse=True)


def calculate_severity_score(unit_data):
    for unit in unit_data:
        unit.severity = unit.flow_count * unit.frequency
        unit.save()
    return unit_data

def is_within_unit(report, unit):
    """
    Determine if the report's coordinates fall within the unit's range.
    This function needs to be adapted based on how you define the range
    and the format of your addresses/coordinates.
    """
    # Assuming coordinates are stored as "latitude,longitude"
    report_coords = tuple(map(float, report.Coordinates.split(',')))
    
    # Example check - this part needs to be tailored to your application
    # For simplicity, let's say we have the center coords of the unit and a radius
    unit_center_coords = (unit.latitude, unit.longitude)  # You need to add these fields to your model
    unit_radius_km = unit.radius_m  # You also need to add this field to your model
    
    # Calculate the distance between the report coords and unit center coords
    distance = geodesic(report_coords, unit_center_coords).miles
    
    # Check if the report is within the unit's radius
    return distance <= unit_radius_km

def calculate_flow_count(report_data):
    point = report_data.Coordinates
    unit = 'mph'
    thickness = 5
    API_KEY = os.environ.get('TOMTOM_API_KEY')
    request_url = f'https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={API_KEY}&point={point}&unit={unit}&thickness={thickness}&openLr=false&jsonp=jsonp'
    response = requests.get(request_url)
    response_data = response.json()
    flow_count = response_data['flowSegmentData']['current']['speed']

    return flow_count

def seed_unit_data():
    return True

def create_unit(report_data):
    try: 
        unit_data = Unit.objects.all()
        for unit in unit_data:
            if is_within_unit(report_data, unit):
                calculate_flow_count = calculate_flow_count(report_data)
                unit.frequency += 1
                unit.save()
                return
        new_unit = Unit()
        new_unit.Address_range_low = report_data.Address
        new_unit.Address_range_high = report_data.Address
    except:
        return False


def update_unit_data(report_data):
    try:
        unit_data = Unit.objects.all()
        for unit in unit_data:
            if is_within_unit(report_data, unit):
                calculate_flow_count = calculate_flow_count(report_data)
                unit.frequency += 1
                unit.save()
        return True
    except:
        return False
