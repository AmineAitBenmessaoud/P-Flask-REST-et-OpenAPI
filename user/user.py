from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3203
HOST = '0.0.0.0'

with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"
@app.route("/users", methods=['GET'])
def get_users():
   return make_response(jsonify(users),200)
@app.route("/movies", methods=['GET'])
def get_movies():
      response = requests.get("http://127.0.0.1:3200/json")
      return response.json()
@app.route("/bookings/<user_id>", methods=['GET'])
def get_bookings(user_id):
   user = [user for user in users if str(user['id']) == str(user_id)]
   print(user)
   if len(user) == 0:
      raise NotFound
   response = requests.get("http://127.0.0.1:3201/bookings/{}".format(user_id))
   return response.json()
@app.route("/moviesinfo/<user_id>", methods=['GET'])
def get_moviesinfo(user_id):
   response = requests.get("http://127.0.0.1:3201/bookings/{}".format(user_id)).json()
   movies_id = []
   dates = response["dates"]
   for date in dates:
      for movie_id in date["movies"]:
         movies_id.append(movie_id)
   movies_info = []
   for movie_id in movies_id:
      movie_response = requests.get("http://127.0.0.1:3200/movies/{}".format(movie_id))
      if movie_response.status_code == 200:
         movies_info.append(movie_response.json())
   return make_response(jsonify(movies_info), 200)
if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
