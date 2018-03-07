# -*- coding: utf-8 -*-

import configparser
import json
import os
import os.path as op
import string
from functools import partial

config = configparser.ConfigParser()
config.read(op.join('geocode', 'sources.ini'))

geocode_sources = {}
for section in config.sections():
    geocode_sources[section] = {}
    geocode_sources[section]['url'] = config.get(section, 'url')
    geocode_sources[section]['lat'] = json.loads(config.get(section, 'lat'))
    geocode_sources[section]['long'] = json.loads(config.get(section, 'long'))

print(geocode_sources)

vars = {
    'api_key_googlemaps' : os.environ.get('API_KEY_GOOGLEMAPS'),
    'api_key_here_id' : os.environ.get('API_KEY_HERE_ID'),
    'api_key_here_code' : os.environ.get('API_KEY_HERE_CODE')
}

def get_url_gen():

    def partial_functor(source):
        s = source['url'].format
        s = partial(s, **vars)
        return s,source['lat'],source['long']

    formated = [partial_functor(geocode_sources[source]) for source in geocode_sources]

    return formated
