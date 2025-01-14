from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3201
HOST = '0.0.0.0'

with open('{}/databases/bookings.json'.format("."), "r") as jsf:
   bookings = json.load(jsf)["bookings"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Booking service!</h1>"
@app.route("/bookings", methods=['GET'])
def get_bookings():
   return make_response(jsonify(bookings),200)
@app.route("/bookings/<userid>", methods=['GET'])
def get_bookings_byuserid(userid):
   for booking in bookings:
      if str(booking["userid"])==str(userid):
         res = make_response(jsonify(booking),200)
         return res
   return  make_response(jsonify("error date not found"),400)
@app.route("/showmovies/<date>", methods=['GET'])
def get_movie_bydate(date):
   response = requests.get("http://127.0.0.1:3202/showmovies/{}".format(date))
   return response.json()
@app.route("/bookings/<userid>", methods=['POST'])
def add_bookings_byuserid(userid):
   req = request.get_json()
   for booking in bookings:
      if str(booking["userid"])==str(userid):
         if(str(req)==str(booking["dates"])):
            return make_response(jsonify({"error : an existing item already exists"}),409)
         else :
            booking["dates"].append(req)
   write(bookings)
   res = make_response(jsonify({"message":"movie added"}),200)
   return res
def write(bookings):
    with open('{}/databases/bookings.json'.format("."), 'w') as f:
        json.dump({"bookings ":  bookings}, f)
if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
