from django.shortcuts import render
from django.http import HttpResponse
from main.forms import CityForm
from main.models import City
from main.helper import get_weather_data

def index(request):
	form = CityForm()

	if request.method == 'POST':
		form = CityForm(request.POST)
		if form.is_valid():
			form.save()
			lat = form.cleaned_data.get('lat')
			lon = form.cleaned_data.get('lon')
			weather_data = get_weather_data(lat, lon)
	elif request.method == 'GET':
		try:
			lat = City.objects.latest('date_added').lat
			lon = City.objects.latest('date_added').lon
			weather_data = get_weather_data(lat, lon)
		except Exception as e:
			weather_data = None

	context = {'form': form, 'weather_data': weather_data}
	return render(request, 'main/index.html', context=context)

