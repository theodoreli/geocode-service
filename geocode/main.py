#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import urllib.request

from flask import Flask
from flask import Response

from geocode_sources import *

app = Flask(__name__)

def request(adr):
    url_collection = get_url_gen()
    print(url_collection)
    for url in url_collection:
        try:
            print(url)
            new = url[0](adr=adr)
            print(new)
            with urllib.request.urlopen(new) as f:
                res = f.read().decode('utf-8')
                json_data = json.loads(res)
                # print(json.dumps(json_data, indent=4, sort_keys=True))

                lat = json_data
                for k in url[1]:
                    lat = lat[k]

                lng = json_data
                for k in url[2]:
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
