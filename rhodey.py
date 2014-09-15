#!/usr/bin/env python
# -*- mode: python; encoding: utf-8 -*-

# flask libraries
from flask import abort, redirect, url_for

# data specific libraries
import urllib2
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  #example redirect
  return redirect(url_for('helloworld'))

@app.route("/helloworld")
def helloworld():
  return "Hello World!"

if __name__ == "__main__":
  #app.debug = True
  app.run()
