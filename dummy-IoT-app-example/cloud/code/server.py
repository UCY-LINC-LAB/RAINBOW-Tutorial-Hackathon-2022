import json
import os
from threading import Thread
from time import sleep

import requests
from flask import Flask
app = Flask(__name__)


# Return data to the browser
@app.route("/", methods=['GET'])
def get():
    # TODO retrieve the computed results
    return "The current status of the data is: ... "


# Offline thread for overall IoT metrics collection
def aggregate():
    edge_servers = os.getenv("EDGE_SERVERS").split(",")
    periodicity = int(os.getenv("COMPUTE_PERIODICITY", 20))
    while True:
        sleep(periodicity)  # waits for some seconds

        # ---- aggregation from all edge servers ----

        for edge_node in edge_servers:
            # TODO Request the data from the edge servers
            # TODO Add logic for final aggregation here
            pass
        # ------------------------------------------
        # TODO store the results


if __name__ == '__main__':

    # Thread execution
    collector_thread = Thread(target=aggregate)
    collector_thread.start()

    # Server execution
    app.run(debug=False, host="0.0.0.0", port=8000)


