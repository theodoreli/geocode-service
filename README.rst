Geocode Service
==================

Geocode Service is a Python server that will geocode an address that you pass in. That is:
1. Via the REST interface, input the address after the `geocode` noun
2. The server will return a JSON response with the geocode

There are Geocode service sources encoded in `sources.ini` that this service will try in the order defined. The service will return the result
of the first service that is succesful. Otherwise, the service returns an error.

Setup
------------

These instructions are for OS X and it probably works on Linux as well.
You need Python 3 and Virtualenv installed.

Create the virtual environment and install the dependencies with:

    $ ./RUN build


Running
-------------

Ensure that you have a credentials file `creds.sh` that exports the required
environment variables so that our app can access the various geocode sources.

An example `creds.sh` file:

.. code-block:: bash

    export API_KEY_GOOGLEMAPS=your_google_key
    export API_KEY_HERE_ID=your_here_key
    export API_KEY_HERE_CODE=_your_here_key

Start the server with the run script:

    $ ./RUN serve

Then send an http GET request to the server in another terminal (or whichever is your preferred way):

    $ curl localhost:5000/geocode/1600+Amphitheatre+Parkway,+Mountain+View,+CA
    {"address_requested": "1600+Amphitheatre+Parkway,+Mountain+View,+CA", "geocoded_address": {"latitude": 37.4224082, "longitude": -122.0856086, "source": "google"}}
