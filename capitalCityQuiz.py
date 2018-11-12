import urllib.parse
import urllib.request
import json

#
#  Quiz on capital cities
#  using API to find countries and their
#  capital city
#


#
# Block of code copied and modified from josh's code
#
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

    )

#
#
#

