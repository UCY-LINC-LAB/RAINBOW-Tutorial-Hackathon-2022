import json
from flask import Flask, request

app = Flask(__name__)

# This class works as in-memory storage
class InMemoryStorage:
    _SUM = 0
    _COUNT = 0

    @classmethod
    def get_sum(cls):
        return float(cls._SUM)

    @classmethod
    def get_count(cls):
        return float(cls._COUNT)

    @classmethod
    def set_sum(cls, _sum):
        cls._SUM = _sum

    @classmethod
    def set_count(cls, _count):
        cls._COUNT = _count

    @classmethod
    def increase_count(cls, value):
        cls.set_count(float(cls._COUNT) + float(value))

    @classmethod
    def increase_sum(cls, value):
        cls.set_sum(float(cls._SUM) + float(value))


#  initialize the variables
InMemoryStorage.set_sum(0)
InMemoryStorage.set_count(0)


@app.route("/", methods=['POST'])
def compute():

    # for each incoming data
    data = json.loads(str(request.data.decode(encoding='utf-8')))

    # compute sum of the trip distances
    InMemoryStorage.increase_sum(data['trip_distance'])

    # and compute count
    InMemoryStorage.increase_count(1)

    return "{'success':'true'}"


@app.route("/", methods=['GET'])
def get_data():

    # when the cloud server requests the data
    # edge/IoT devices retrieve the data
    res = dict(sum=InMemoryStorage.get_sum(), count=InMemoryStorage.get_count())

    # initiate the sum and count again to 0
    InMemoryStorage.set_sum(0)
    InMemoryStorage.set_count(0)

    # You need to expose the sum to the RAINBOW monitoring stack
    # You need to add an environmental variable (RAINBOW_AGENT_HOST) which is the IP of the RAINBOW monitoring agent
    # #  TODO add your RAINBOW code here
    # An example of custom metric expose
    # from RainbowMonitoringSDK.utils.annotations import RainbowUtils
    # RainbowUtils.store(float(random.uniform(0, 100)), # value
    #                           'random_generated_number', # name
    #                           'rad',  # units e.g., bps, mb, etc.
    #                           'Randomly generated number')  # description


    # return the retrieved data to Cloud
    return json.dumps(res)


if __name__ == '__main__':

    # execute the server
    app.run(debug=False, host="0.0.0.0", port=8000)