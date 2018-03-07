#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.request

from flask import Flask
from flask import Response

from geocode_sources import *

app = Flask(__name__)

geocode_sources = GeocodeSources()
sources_dict = geocode_sources.get_sources_dict()
print(sources_dict)

def request(adr):
    for source in sources_dict:
        try:
            new = sources_dict[source]['url'](adr=adr)
            with urllib.request.urlopen(new) as f:
                res = f.read().decode('utf-8')
                json_data = json.loads(res)
                print(json.dumps(json_data, indent=4, sort_keys=True))

                lat = json_data
                for k in sources_dict[source]['lat']:
                    lat = lat[k]

                lng = json_data
                for k in sources_dict[source]['long']:
                    lng = lng[k]

                return lat,lng
        except:
            print('error')


@app.route('/')
def index():
    # give instructions
    pass

@app.route('/geocode/<address>')
def get_geocode(address):
    lat,lng = request(address)
    #return str(lat) + ',' + str(lng)
    return '{},{}'.format(str(lat),str(lng))

if __name__ == '__main__':
    app.run()
