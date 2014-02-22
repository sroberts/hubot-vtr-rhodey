hubot-vtr-rhodey
================

Helper service for Hubot-VTR

## Setup
* First you'll need to install [Flask](http://flask.pocoo.org/) using either ```pip install flask``` or ```easy_install flask```.
* Second you'll need MaxMind's GeoIP City setup. You can [get directions to do that here](http://dev.maxmind.com/geoip/legacy/install/city/). After that's done make sure the ```GeoLiteCity.dat``` file is in the ```/data``` directory.

## Running
Couldn't be simpler, just run ```python rhodey.py``` and now you can go to http://localhost:5000/helloworld to make sure it's working.
