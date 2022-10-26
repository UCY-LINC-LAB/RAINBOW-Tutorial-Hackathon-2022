import json
import os
from time import sleep
import requests
import pandas as pd

if __name__ == "__main__":

    # set the periodicity based on IOT_DATA_GENERATION_PERIODICITY environmental variable
    periodicity = int(os.getenv("IOT_DATA_GENERATION_PERIODICITY", 5))

    df = pd.read_parquet("/data/yellow_tripdata_2022-04.parquet")  # retrieve the dataset

    while True:
        sleep(periodicity)

        # indicates how many datapoints will send the workload in each run
        data_size = int(os.getenv("IOT_DATA_SIZE", 1))
        edge_node = os.getenv("TARGET_EDGE")  # The edge server that the workload generator is connected to

        # ----- data fetching ----------
        data = df.sample(n=data_size)
        fields = [
            'passenger_count', 'trip_distance', 'RatecodeID',
            'store_and_fwd_flag', 'PULocationID', 'DOLocationID',
            'payment_type', 'fare_amount', 'extra', 'mta_tax',
            'tip_amount', 'tolls_amount', 'improvement_surcharge',
            'total_amount', 'congestion_surcharge', 'airport_fee'
            ]
        data = data[fields]
        data = data.to_dict(orient='records')
        # -----------------------------------

        # ----- data dissemination ----------
        try:
            for i in data:
                requests.post("http://%s:8000/" % edge_node, data=json.dumps(i), timeout=10)
        except:
            print("IoT Data is lost.")
        # -------------------------------------
