import feedparser
import urllib.parse
import urllib.request
import json
import datetime

### key = 7a82ee6f4ab290329464c1a55194b4ab

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '7a82ee6f4ab290329464c1a55194b4ab'
    unit = 'metric'
    api = 'http://api.openweathermap.org/data/2.5/weather?id='

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_data):
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = dict(
        city=raw_data.get('name'),
        country=sys.get('country'),
        temp=main.get('temp'),
        temp_max=main.get('temp_max'),
        temp_min=main.get('temp_min'),
        humidity=main.get('humidity'),
        pressure=main.get('pressure'),
        sky=raw_data['weather'][0]['main'],
        sunrise=time_converter(sys.get('sunrise')),
        sunset=time_converter(sys.get('sunset')),
        wind=raw_data.get('wind').get('speed'),
        wind_deg=raw_data.get('deg'),
        dt=time_converter(raw_data.get('dt')),
        cloudiness=raw_data.get('clouds').get('all')
    )
    return data

def data_output(data):
    data['m_symbol'] = '\xb0' + 'C'
    s = '''---------------------------------------
Current weather in: {city}, {country}:
{temp}{m_symbol} {sky}
Max: {temp_max}, Min: {temp_min}

Wind Speed: {wind}, Degree: {wind_deg}
Humidity: {humidity}
Cloud: {cloudiness}
Pressure: {pressure}
Sunrise at: {sunrise}
Sunset at: {sunset}

Last update from the server: {dt}
---------------------------------------'''
    print(s.format(**data))


if __name__ == '__main__':
    try:
        data_output(data_organizer(data_fetch(url_builder(2172797))))
    except IOError:
        print('no internet')
