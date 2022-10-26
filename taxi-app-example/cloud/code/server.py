import json
import os
from threading import Thread
from time import sleep

import requests
from flask import Flask
app = Flask(__name__)


# This class works as in-memory storage
class LastAverageDistance:

    @classmethod
    def set_distance(cls, value):
        os.environ["LAST_AVERAGE_DISTANCE"] = value

    @classmethod
    def get_distance(cls):
        return os.environ["LAST_AVERAGE_DISTANCE"]


# Data initialization
LastAverageDistance.set_distance("It is not computed yet")


# Return data to the browser
@app.route("/", methods=['GET'])
def get():
    return "The latest average distance is: "+LastAverageDistance.get_distance()


# Offline thread for overall IoT metrics collection
def aggregate():
    edge_servers = os.getenv("EDGE_SERVERS").split(",")
    periodicity = int(os.getenv("COMPUTE_PERIODICITY", 20))
    while True:
        sleep(periodicity)  # waits for some seconds

        # ---- aggregation from all edge servers ----
        _sum = 0
        _count = 0
        for edge_node in edge_servers:
            data = requests.get("http://%s:8000/" % edge_node, timeout=10)
            data = json.loads(data.text)
            _sum += float(data['sum'])
            _count += float(data['count'])
        # ------------------------------------------

        if _count > 0:
            LastAverageDistance.set_distance(str(_sum/_count))  # cache the result to storage


if __name__ == '__main__':

    # Thread execution
    collector_thread = Thread(target=aggregate)
    collector_thread.start()

    # Server execution
    app.run(debug=False, host="0.0.0.0", port=8000)


