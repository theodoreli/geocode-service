# -*- coding: utf-8 -*-

import json
import logging
import urllib.request

from geocode_sources import GeocodeSources

L = logging.getLogger()

class Request():
    def __init__(self):
        geocode_sources = GeocodeSources()
        self.sources_dict = geocode_sources.get_sources_dict()

    def request(self, adr):
        for source in self.sources_dict:
            try:
                formatted_url = self.sources_dict[source]['url'](adr=adr)
                with urllib.request.urlopen(formatted_url) as f:
                    res = f.read().decode('utf-8')
                    json_data = json.loads(res)
                    L.debug(json.dumps(json_data, indent=4, sort_keys=True))

                    lat = json_data
                    for k in self.sources_dict[source]['lat']:
                        lat = lat[k]

                    lng = json_data
                    for k in self.sources_dict[source]['long']:
                        lng = lng[k]

                    return lat,lng
            except:
                L.info('Error in source {}'.format(source))
