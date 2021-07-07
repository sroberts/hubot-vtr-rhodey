#!/usr/bin/env python
# -*- mode: python; encoding: utf-8 -*-

# flask libraries
from flask import abort, redirect, url_for

# data specific libraries
import urllib2
import json
import requests
from bs4 import BeautifulSoup as bs

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
  #example redirect
  return redirect(url_for('helloworld'))


@app.route("/helloworld")
def helloworld():
  return "Hello World!"


@app.route("/ip/<ip>/geo/maxmind.json")
def maxmindgeoip(ip):
  gir = gi.record_by_addr(ip)
  return '%s' % json.dumps(gir)


@app.route("/ip/<ip>/geo/ipinfo.json")
def geoip_ipinfo(ip):

  f = urllib2.urlopen('http://ipinfo.io/%s/json' % (ip))
  return '%s' % f.read()


@app.route("/ip/<ip>/ipvoid/ipvoid.json")
def ipvoid(ip):
    r = requests.get('http://www.ipvoid.com/scan/'+ip+'/')
    data = bs(r.text)
    return_list = []
    if data.findAll('span', attrs={'class': 'label label-success'}):
        return "Site is clean according to latest scan"
    elif data.findAll('span', attrs={'class': 'label label-danger'}):
        for each in data.findAll('img', alt='Alert'):
            detect_site = each.parent.parent.td.text.lstrip()
            detect_url = each.parent.a['href']
            return_list.append({'site': detect_site, 'info_url': detect_url})
    else:
        return "Could not find a decision"
    return '%s' % json.dumps(return_list)


@app.route("/name/<name>/url/urlvoid.json")
def urlvoid(name):
    r = requests.get('http://www.urlvoid.com/scan/'+name+'/')
    data = bs(r.text)
    return_list = []
    if data.findAll('div', attrs={'bs-callout bs-callout-info'}):
        return "Site is clean according to latest scan"
    elif data.findAll('div', attrs={'class': 'bs-callout bs-callout-warning'}):
        for each in data.findAll('img', alt='Alert'):
            detect_site = each.parent.parent.td.text.lstrip()
            detect_url = each.parent.a['href']
            return_list.append({'site': detect_site, 'info_url': detect_url})
    else:
        return "Could not find a decision"
    if len(return_list) == 0:
        return "No major warning for site"
    return '%s' % json.dumps(return_list)


if __name__ == "__main__":
  #app.debug = True
  app.run()
