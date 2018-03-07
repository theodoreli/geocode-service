# -*- coding: utf-8 -*-

import configparser
import json
import os
import os.path as op
import string
from functools import partial

vars = {
    'api_key_googlemaps' : os.environ.get('API_KEY_GOOGLEMAPS'),
    'api_key_here_id' : os.environ.get('API_KEY_HERE_ID'),
    'api_key_here_code' : os.environ.get('API_KEY_HERE_CODE')
}

class GeocodeSources():
    def __init__(self):
        config = configparser.ConfigParser()
        # TODO: solidify this read
        config.read(op.join('geocode', 'sources.ini'))

        self.geocode_sources = {}
        gs = self.geocode_sources
        for section in config.sections():
            gs[section] = {}
            gs[section]['url'] = (config.get(section, 'url')).format
            gs[section]['url'] = partial(gs[section]['url'], **vars)

            gs[section]['lat'] = json.loads(config.get(section, 'lat'))
            gs[section]['long'] = json.loads(config.get(section, 'long'))


    def get_sources_dict(self):
        return self.geocode_sources
