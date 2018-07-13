from flask import Flask, render_template, send_from_directory
import os
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("82.165.16.151")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", to="Sam Moorhouse")

@app.route('/btn')
def btn():
    print("button clicked")
    client.publish("test/all", "this is my message to you")
    return ""

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/whereami')
def whereami():
	return "Kdua"

@app.route('/hello/<name>')
def foo(name):
    return render_template('index.html', to=name)


