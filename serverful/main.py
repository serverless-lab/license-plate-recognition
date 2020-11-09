# encoding: utf-8

import base64
import cv2
import hyperlpr
import numpy as np
import requests
from flask import Flask, request

app = Flask(__name__)


def licence_plate_parser(img_base64: str):
    base64data = base64.b64decode(img_base64.encode("utf8"))
    nparr = np.fromstring(base64data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return {
        "result": hyperlpr.HyperLPR_plate_recognition(img)
    }


@app.route("/lpr", methods=["GET"])
def index():
    img = request.args.get("image")
    if img is None:
        return {"message": "image base64 required."}
    return licence_plate_parser(img)


@app.route("/test", methods=["GET"])
def test():
    with open("test.jpg", "rb") as f:
        base64data = base64.b64encode(f.read())

    img_base64 = base64data.decode("utf8")
    resp = requests.get("localhost:5000/lpr", params={"image": img_base64})
    return resp.json()


if __name__ == '__main__':
    app.run()
