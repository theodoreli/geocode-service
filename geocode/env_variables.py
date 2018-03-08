# -*- coding: utf-8 -*-
'''Dictionaries of all environment variables.'''

import os

# Environment variables for the application.
env_app_dict = {
    'debug': os.environ.get('APP_DEBUG'),
    'port': os.getenv('APP_PORT', 5000),
}

# Environment variables for the geocode source API.
env_api_dict = {
    'api_key_googlemaps': os.environ.get('API_KEY_GOOGLEMAPS'),
    'api_key_here_id': os.environ.get('API_KEY_HERE_ID'),
    'api_key_here_code': os.environ.get('API_KEY_HERE_CODE')
}
