#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys

from flask import Flask

from request import request

L = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
if os.environ.get('APP_DEBUG') == 'true':
    L.setLevel(logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def index():
    help = ('Hit the endpoint /geocode/<address> where address is the string'
            ' you want to Geocode')
    return help


@app.route('/geocode/<address>')
def get_geocode(address):
    '''Given an address, return the lattitude and longitude as a string'''
    L.info('Received address: {}'.format(address))
    lat, lng = request(address)

    lat_long = '{},{}'.format(str(lat), str(lng))
    L.info('Latitude and Logitude respectively: {}'.format(lat_long))

    return lat_long


if __name__ == '__main__':
    L.info('Starting Flask application')
    app.run()
