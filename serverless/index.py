# encoding: utf-8

import base64
import json
import cv2
import hyperlpr
import numpy as np


def licence_plate_parser(img_base64: str):
    base64data = base64.b64decode(img_base64.encode("utf8"))
    nparr = np.fromstring(base64data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return {
        "result": hyperlpr.HyperLPR_plate_recognition(img)
    }


def handler(environ, start_response):
    try:
        query_string = environ['QUERY_STRING']
        img_base64 = query_string.split("=")[1]
        result = licence_plate_parser(img_base64)
    except (KeyError):
        result = {"message": "image base64 required."}

    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)
    return [json.dumps(result).encode("utf8")]


def handler_test(environ, start_response):
    with open("test.jpg", "rb") as f:
        base64data = base64.b64encode(f.read())
    img_base64 = base64data.decode("utf8")

    result = licence_plate_parser(img_base64)
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)
    return [json.dumps(result).encode("utf8")]
