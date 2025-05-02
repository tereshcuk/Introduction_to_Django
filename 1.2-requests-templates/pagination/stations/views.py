from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице     
    page_number = int(request.GET.get('page', 1))
    
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        content = csv.DictReader(csvfile) 
        bus_stations_list = []
        for row in content:
            bus_stations_list.append(row)            
    
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)    
    context = {
                   'bus_stations': page.object_list,
                   'page': page,
                  }    
   
    return render(request, 'stations/index.html', context)
