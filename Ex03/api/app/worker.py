#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import sys
import requests
import redis


ELASTIC = os.environ['ELASTIC']
APP = Flask(__name__)
CORS(APP)

@APP.route('/ping', methods=['GET'])
@cross_origin()
def ping() :
    return Response("pong",mimetype='text/html')

@APP.route('/test_elastic', methods=['GET'])
@cross_origin()
def test_elastic():
    res = requests.put("http://" + ELASTIC + ":9200/magic_powua")
    print(res.json, file=sys.stderr)
    return (jsonify(res.json()))

@APP.route('/test_redis', methods=['GET'])
@cross_origin()
def test_redis():
    r = redis.Redis(host="redis", port=6379)
    try:
        data = json.dumps({"data" : "GNE GNE"})
        r.mset({"index2" : data})
        return ("ok")
    except:
        return ("ko")

if __name__ == "__main__":

    r = redis.Redis(host="redis", port=6379)
    try:
        data = json.dumps({"data" : "GNE GNE"})
        r.mset({"index1" : data})
        print("Redis is Working")
    except Exception as e:
        print(e)
        sys.exit(84)
    try :
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
