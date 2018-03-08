# -*- coding: utf-8 -*-

import json
import logging
import urllib.request

from geocode_sources import get_sources_dict

L = logging.getLogger()

sources_dict = get_sources_dict()


def request(adr):
    '''Given an addreess, request the geocode.

    In the case that one geocoding source is not accessible, there are
    multiple sources that are available in `sources_dict`.

    Note that the `url` key of `sources_dict` is a partially formatted
    string. This saves us time in that we only need to format a subset of
    values upon receiving a request.
    '''
    for key, value in sources_dict.items():
        try:
            # Format the partially formatted `url` string.
            formatted_url = value['url'](adr=adr)

            with urllib.request.urlopen(formatted_url) as f:
                res = f.read().decode('utf-8')
                json_data = json.loads(res)
                L.debug(json.dumps(json_data, indent=4, sort_keys=True))

                # Traverse the structure to access latitude.
                lat = json_data
                for k in value['lat']:
                    lat = lat[k]

                # Traverse the structure to access longitude.
                long = json_data
                for k in value['long']:
                    long = long[k]

                data = {'address_requested': adr,
                        'geocoded_address': {'latitude': lat,
                                             'longitude': long,
                                             'source': key}}

                return data

        except BaseException as ex:
            L.info('Geocode source "{}" produced error: {}'.
                   format(key, ex))
    else:
        return {'error': 'Not able to geocode address'}
