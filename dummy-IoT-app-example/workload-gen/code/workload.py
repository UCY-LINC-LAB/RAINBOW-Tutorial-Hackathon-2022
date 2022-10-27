import json
import os
from time import sleep
import requests
import pandas as pd

if __name__ == "__main__":

    # set the periodicity based on IOT_DATA_GENERATION_PERIODICITY environmental variable
    periodicity = int(os.getenv("IOT_DATA_GENERATION_PERIODICITY", 5))

    # TODO retrieve the stored dataset

    while True:
        sleep(periodicity)

        # TODO Retrieve the IoT datapoints

        # ----- data dissemination ----------
        try:
            # TODO Send datapoints to respective edge node
            # for i in data:
            #     requests.post("http://%s:8000/" % edge_node, data=json.dumps(i), timeout=10)
            pass
        except:
            # TODO Handle communication Exception
            pass
        # -------------------------------------
