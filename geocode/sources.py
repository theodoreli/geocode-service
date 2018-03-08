# -*- coding: utf-8 -*-
'''Parse and partially format Geocode Sources from `config.ini`.'''

import configparser
import json
import os.path as op
from functools import partial

from env_variables import env_api_dict


def get_sources_dict():
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

    gs = {}  # Geocode Sources dictionary.
    for section in config.sections():  # eg. ['google', 'here'].
        gs[section] = {}

        # Partially format the url.
        gs[section]['url'] = (config.get(section, 'url')).format
        gs[section]['url'] = partial(gs[section]['url'], **env_api_dict)

        gs[section]['lat'] = json.loads(config.get(section, 'lat'))
        gs[section]['long'] = json.loads(config.get(section, 'long'))

    return gs
