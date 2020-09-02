#!/bin/python3

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

inventory = [
    {
        "name": "toothpaste",
        "quantity": 100
    },
    {
        "name": "perfume",
        "quantity": 25
    },
    {
        "name": "soap",
        "quantity": 50
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/v1/get/all', methods=['GET'])
def getAll():
    return jsonify(inventory)

@app.route('/v1/get', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for item in inventory:
        if item['name'] == name:
            results.append(item)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run(host="0.0.0.0")