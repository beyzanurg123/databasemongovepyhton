import base64
import datetime
from flask import Flask, jsonify, render_template, request, redirect, session
import pymongo
from bson.json_util import ObjectId
import json


class ObjectIdEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(ObjectIdEncoder, self).default(obj)


app =Flask(__name__)
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["okuldb"]
app.json_encoder=ObjectIdEncoder

@app.route('/aldıgıdersler')
def aldıgıdersler():
    aldıgıdersler={"res":list(mydb["aldıgıdersler"].find({}).sort("_id",pymongo.DESCENDING))}
    return jsonify(aldıgıdersler)


@app.route('/')
def index():
       return "mobil"

@app.route('/api')
def apı():
    mydata={"msg":'apımessage'}
    return jsonify(mydata)

@app.route('/ogrencıler')
def apı_request():
    mydataa={"msg":'apımessage'}
    return jsonify(mydataa)


@app.route('/devmszlk')
def devmszlk():
    devmszlk=list(mydb["devmszlk"].find({}))
    return jsonify(devmszlk)

if __name__=="__main__":
    app.run(debug=True)