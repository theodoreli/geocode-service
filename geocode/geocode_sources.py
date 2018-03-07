# -*- coding: utf-8 -*-

import os
import string
from functools import partial

vars = {
    'api_key_googlemaps' : os.environ.get('API_KEY_GOOGLEMAPS'),
    'api_key_here_id' : os.environ.get('API_KEY_HERE_ID'),
    'api_key_here_code' : os.environ.get('API_KEY_HERE_CODE')
}

def get_url_gen():

    urls = [
            (('https://maps.googleapis.com/maps/api/geocode/json?'
             'address={adr}&key={api_key_googlemaps}'),
             ['results', 0, 'geometry', 'location', 'lat'],
             ['results', 0, 'geometry', 'location', 'lng']),
            ('https://geocoder.cit.api.here.com/6.2/geocode.json?app_id={api_key_here_id}&app_code={api_key_here_code}&searchtext={adr}', [], [])
    ]

    def partial_functor(x):
        s = x[0].format
        s = partial(s, **vars)
        return s,x[1],x[2]

    formated = [partial_functor(url) for url in urls]
    return formated



    #'https://map.googleapis.com/maps/api/geocode/json?address={adr}&key={api_key_googlemaps}'.format(api_key_googlemaps=api_key_googlemaps)



    #return urls


'''
    urls.append('https://geocoder.cit.api.here.com/6.2/geocode.json?app_id={id}&app_code={code}&searchtext={adr}'.format(id=api_key_here_id,
                                              code=api_key_here_code,
                                              adr=values['adr']))
                                              '''

