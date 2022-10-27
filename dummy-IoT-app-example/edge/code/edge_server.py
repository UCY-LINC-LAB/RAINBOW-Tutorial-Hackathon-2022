import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def compute():
    # TODO Add partial aggregation logic here
    return "{'success':'true'}"


@app.route("/", methods=['GET'])
def get_data():
    # TODO return the aggregated data
    return "{}"


if __name__ == '__main__':

    # execute the server
    app.run(debug=False, host="0.0.0.0", port=8000)