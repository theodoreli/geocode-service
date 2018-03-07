Geocode Service
==================

Geocode Service is a Python server that will geocode an address that you pass in. That is, it will return the longitude and lattitude
of a given address.

There are Geocode service sources encoded in `sources.ini` that this service will try in the order defined. The service will return the result
of the first service that is succesful. Otherwise, the service returns an error.

Setup
------------

These instructions are for OS X and it probably works on Linux as well.
You need Python 3 and Virtualenv installed


    $ pip install virtualenv
    $ ./RUN build
    
Be sure to also drop in your credentials (TODO: codify this)


Running
-------------

Start the server with the run script

    ./RUN serve

Then send an http GET request to the server in another terminal (or whichever is your preferred way)

    $ curl localhost:5000/geocode/1600+Amphitheatre+Parkway,+Mountain+View,+CA
    37.4224082,-122.0856086
