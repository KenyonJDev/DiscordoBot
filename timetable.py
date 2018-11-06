import urllib.parse
import urllib.request
import json

def url_builder(location,transport):
    app_key = 'bd5f386fb6fbac9344fc1c4e41f48002'
    app_id = 'd1a1cdb4'
    api = 'http://transportapi.com/v3/uk/places.json?query='

    full_url = api + str(location)+'&type=' + str(transport)+'&app_id=' + app_id + '&app_key='+ bd5f386fb6fbac9344fc1c4e41f48002
    return full_url

# example URL: http://transportapi.com/v3/uk/places.json?query=euston&type=train_station&app_id=d1a1cdb4&app_key=bd5f386fb6fbac9344fc1c4e41f48002

def data_fetch(full_url):
    url = urllib.request.urlopen(full_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict

def data_organiser(raw_data):
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = dict(
        type=raw_data.get('type'),
        name=sys.get('name'),
        latitude=main.get('latitude'),
        longitude=main.get('longitude'),
        accuracy=main.get('accuracy'),
        source=main.get('source'),
        request_time=main.get('request_time'),
        station_code=main.get('station_code')
    )

def data_output(data):
    s = '''-----------------------------------
    station name: {name} {type}:
    station code: {station_code}
    Latitude:{latitude}
    Longitude:{longitude}
    accuracy: {accuracy}
    
    Source: {source}
    Requested {request_time}
    -----------------------------------'''
    print(s.format(**data))
    
