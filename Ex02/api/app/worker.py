#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
## EPITECH PROJECT, 2020
## WorshopHub
## File description:
## worker
##

import json
import os
import requests
import random
import sys

from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

ELASTIC = os.environ['ELASTIC']
APP = Flask(__name__)
CORS(APP)

@APP.route('/ping', methods=['GET'])
@cross_origin()
def ping():
    return Response("pong",mimetype='text/html')

@APP.route('/test', methods=['GET'])
@cross_origin()
def test():
    res = requests.put("http://" + ELASTIC + ":9200/magic_powua")
    print(res.json, file=sys.stderr)
    return (jsonify(res.json()))

if __name__ == "__main__":

    try :
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
