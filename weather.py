import urllib.parse
import urllib.request
import json
import datetime#

### key = 7a82ee6f4ab290329464c1a55194b4ab

def checkWeather(stringInp):
    weatherOut = url_builder(stringInp)
    return weatherOut

def time_converter(time): #This converts the time that openweathermap provides us
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '7a82ee6f4ab290329464c1a55194b4ab' #the key I generated from openweathermaps
    unit = 'metric' #leave this blank for fahrenheit
    api = 'http://api.openweathermap.org/data/2.5/weather?q='
    
    
    
    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url
    
### example url = http://api.openweathermap.org/data/2.5/weather?q=London,uk%27&mode=json&units=metric&appid=7a82ee6f4ab290329464c1a55194b4ab


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organiser(raw_data):
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = dict(
        city=raw_data.get('name'),
        country=sys.get('country'),
        temp=main.get('temp'),
        humidity=main.get('humidity'),      
        sky=raw_data['weather'][0]['main'],
        wind=raw_data.get('wind').get('speed'),
        dt=time_converter(raw_data.get('dt')),
        cloudiness=raw_data.get('clouds').get('all')
    )
    return data

def data_output(data):
    data['m_symbol'] = '\xb0' + 'C'
    weatheroutput = '''-----------------------------------
    :sunrise_over_mountains: 
Current weather in {city}, {country}:
{temp}{m_symbol} {sky}

Wind Speed: {wind}km/h
Humidity: {humidity}
Cloud: {cloudiness}

Updated: {dt}
-----------------------------------'''
    return weatheroutput.format(**data)


def weatherInit(userInp):
    try:
        location = userInp.lower().replace("weather ", '')
        return data_output(data_organiser(data_fetch(url_builder(location))))
    except IOError:
        print("Sorry, I don't know what you mean")
