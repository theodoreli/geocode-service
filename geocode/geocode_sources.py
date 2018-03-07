# -*- coding: utf-8 -*-

import configparser
import json
import os
import os.path as op
from functools import partial

class GeocodeSources():
    env_vars = {
        'api_key_googlemaps' : os.environ.get('API_KEY_GOOGLEMAPS'),
        'api_key_here_id' : os.environ.get('API_KEY_HERE_ID'),
        'api_key_here_code' : os.environ.get('API_KEY_HERE_CODE')
    }

    def __init__(self):
        '''Construct a dictionary that contains our geocode sources.

        An example of a source key value pair is the following:
        source : {
                    url: `url of geocode source`
                    lat: `Path to traverse for returned JSON to get Lattitude`
                    long: `Path to traverse for returned JSON to get Longitude`
                  }
        '''
        config = configparser.ConfigParser()
        curr_dir = op.dirname(op.realpath(__file__))
        config.read(op.join(curr_dir, 'sources.ini'))

        self.geocode_sources = {}
        gs = self.geocode_sources # eg. ['google', 'here']
        for section in config.sections():
            gs[section] = {}

            # Partially format the url.
            gs[section]['url'] = (config.get(section, 'url')).format
            gs[section]['url'] = partial(gs[section]['url'], **self.env_vars)

            gs[section]['lat'] = json.loads(config.get(section, 'lat'))
            gs[section]['long'] = json.loads(config.get(section, 'long'))

    def get_sources_dict(self):
        return self.geocode_sources
