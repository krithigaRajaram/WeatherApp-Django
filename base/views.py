from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm
# Create your views here.
def index(request):
    context={}
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=69a657b8f20295cc2f14ccd7bc71dfd1'
    if request.method == 'POST':
        form=CityForm(request.POST)
        form.save()
    form= CityForm()

    cities = City.objects.all()
    data=[]
    for city in cities:
    
   
        r=requests.get(url.format(city)).json()
        city_weather={
            'city':city,
            'temperature' : r['main']['temp'],
            'description': r['weather'][0]['description'],            
            'icon':r['weather'][0]['icon'],
        }
        data.append(city_weather)

    context={'data': data,'form':form}
    return render(request,'base/index.html',context)
