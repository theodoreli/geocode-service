#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os
import sys
import urllib.request

from flask import Flask
from flask import Response

from geocode_sources import GeocodeSources

L = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
if os.environ.get('APP_DEBUG') == 'true':
    L.setLevel(logging.DEBUG)

app = Flask(__name__)

geocode_sources = GeocodeSources()
sources_dict = geocode_sources.get_sources_dict()

def request(adr):
    for source in sources_dict:
        try:
            formatted_url = sources_dict[source]['url'](adr=adr)
            with urllib.request.urlopen(formatted_url) as f:
                res = f.read().decode('utf-8')
                json_data = json.loads(res)
                L.debug(json.dumps(json_data, indent=4, sort_keys=True))

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
    L.info('Received address: {}'.format(address))
    lat,lng = request(address)

    lat_long = '{},{}'.format(str(lat),str(lng))
    L.info('Latitude and Logitude respectively: {}'.format(lat_long))

    return lat_long

if __name__ == '__main__':
    L.info('Starting Flask application')
    app.run()
