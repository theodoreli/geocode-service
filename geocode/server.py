#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
import sys

from flask import Flask

from env_variables import env_app_dict
from request import request

L = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
if env_app_dict['debug'] == 'true':
    L.setLevel(logging.DEBUG)

app = Flask(__name__)
PORT = env_app_dict['port']


@app.route('/')
def index():
    help = ('Hit the endpoint /geocode/<address> where address is the string'
            ' you want to Geocode')
    return help


@app.route('/geocode/<address>')
def get_geocode(address):
    '''Given an address, return the lattitude and longitude as a string'''
    L.info('Received address: {}'.format(address))
    geocoded_data = request(address)
    L.info('Geocoded address: {}'.format(geocoded_data))
    return json.dumps(geocoded_data)


if __name__ == '__main__':
    L.info('Starting Flask application')
    app.run(port=PORT)
