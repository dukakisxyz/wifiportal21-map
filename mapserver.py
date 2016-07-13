from flask import Flask, json, jsonify, render_template, request, g, redirect, url_for
import models
import sqlite3 as lite
import sys

#21 imports
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml

app = Flask(__name__)
payment = Payment(app, Wallet())
app.debug = True



@app.route('/register/<string:description>/<string:latitude>/<string:longitude>')
@payment.required(1000)
def register_location(description = None, latitude=None, longitude=None):
    try:
        description = description.replace("_", " ")
        latitude = float(latitude)
        longitude = float(longitude)

        models.LocationData.add_location(
            description=description,
            latitude=latitude,
            longitude=longitude)
        
        #return json.dumps("success")
        return json.dumps("Your location has been registered successfully and should be immediately available online at 10.244.183.245:8000/map")
    except ValueError:
        return json.dumps("Value Error: Looks like this location is already registered.")

'''
@app.route('/get_payment')
@payment.required(1000)
def payment_accepted():
	return json.dumps("Your location has been registered successfully and should be immediately available online at 10.244.183.245:8000/map")
'''

@app.route('/map')
@app.route('/')
def index():
	return render_template('map.html')

@app.route('/get_location_data')
def send_the_data():
	data = []
	con = lite.connect('locations.db')
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM LocationData")
		rows = cur.fetchall()
		for location in rows:
			location = location[1:4]
			data.append(location)
			

	return json.dumps(data)

@app.route('/documentation')
def info():
	return json.dumps("")


@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)

if __name__ == '__main__':
	models.initialize()
	app.run(host='0.0.0.0', port=5000)
