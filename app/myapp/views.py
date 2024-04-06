from django.shortcuts import render
from django.http import HttpResponse
from .models import Report, Unit

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

