#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import locationiq_key


class LocationIQ(Base):
    """
    LocationIQ Geocoding API
    ===================
    LocationIQ provides 30,000 events per day and uses OpenStreetMaps

    Params
    ------
    :param q: Your search location you want geocoded.
    :param key: LocationIQ API key.
    :param format: json

    References
    ----------
    API Documentation: https://locationiq.org/
    Get LocationIQ Key: https://locationiq.org/#register
    """
    provider = 'locationiq'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://locationiq.org/v1/search.php'
        self.location = location
        self.params = {
            'q': location,
            'format': 'json',
            'key': self._get_api_key(locationiq_key, **kwargs),
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self.parse['lat']

    @property
    def lng(self):
        return self.parse['lon']

    @property
    def latlng(self):
        return [self.lat, self.lng]

    @property
    def bbox(self):
        return self.parse['boundingbox']

    @property
    def importance(self):
        return self.parse['importance']

    @property
    def address_type(self):
        return self.parse['type']

    @property
    def address(self):
        return self.parse.get('display_name')
    

if __name__ == '__main__':
    g = LocationIQ('26 E. 15th, Cincinnati, OH')
    g.debug()
