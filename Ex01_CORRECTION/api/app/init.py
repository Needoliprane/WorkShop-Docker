##
## EPITECH PROJECT, 2020
## WorshopHub
## File description:
## init
##

from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

APP = Flask(__name__)
CORS(APP)

@APP.route('/ping', methods=['GET'])
@cross_origin()
def ping() :
    return Response("pong",mimetype='text/html')

if __name__ == "__main__":

    try :
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
