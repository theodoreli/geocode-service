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
        config.read(op.join('geocode', 'sources.ini'))

        self.geocode_sources = {}
        gs = self.geocode_sources
        for section in config.sections():
            gs[section] = {}
            gs[section]['url'] = config.get(section, 'url')
            gs[section]['lat'] = json.loads(config.get(section, 'lat'))
            gs[section]['long'] = json.loads(config.get(section, 'long'))
        print(gs)


    def get_sources_dict(self):
        def partial_functor(source):
            s = source['url'].format
            s = partial(s, **vars)
            return s,source['lat'],source['long']

        formated = [partial_functor(self.geocode_sources[source]) for source in self.geocode_sources]

        return formated





