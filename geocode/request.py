# -*- coding: utf-8 -*-

import json
import logging
import urllib.request

from geocode_sources import GeocodeSources

L = logging.getLogger()

geocode_sources = GeocodeSources()
sources_dict = geocode_sources.get_sources_dict()


def request(adr):
    '''Given an addreess, request the geocode.

    In the case that one geocoding source is not accessible, there are
    multiple sources that are available in `sources_dict`.

    Note that the `url` key of `sources_dict` is a partially formatted
    string. This saves us time in that we only need to format a subset of
    values upon receiving a request.
    '''
    for source in sources_dict:
        try:
            # Format the partially formatted `url` string.
            formatted_url = sources_dict[source]['url'](adr=adr)

            with urllib.request.urlopen(formatted_url) as f:
                res = f.read().decode('utf-8')
                json_data = json.loads(res)
                L.debug(json.dumps(json_data, indent=4, sort_keys=True))

                lat = json_data
                for k in sources_dict[source]['lat']:
                    lat = lat[k]

                lng = json_data
                for k in sources_dict[source]['long']:
                    lng = lng[k]

                return lat, lng
        except BaseException as ex:
            L.info('Geocode source "{}" produced error: {}'.
                   format(source, ex))
