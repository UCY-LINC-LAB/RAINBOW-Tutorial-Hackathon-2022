
# Description

This repo provides a 3-tier application for aggregating data of a taxi company. The taxis, which are implemented as lightweight containers, periodically send a specific number of data points to the Edge servers (one taxi workload generator is connected to one Edge server).
Each data point represents a taxi trip, and every Edge server computes the sum of trip distances and count of every incoming datapoint.
Finally, Cloud service exists and periodically requests all edge servers, retrieves the metrics, and computes the overall average trip distances and counts. The Cloud server also exposes a simple API call through which users can retrieve the respective results.

## Requirements
Before starting, we have to install docker, docker-compose, and docker swarm on the infrastructure.
For more information, we suggest the official [documentation](https://docs.docker.com/).
For the IoT dataset, users have to download the file `yellow_tripdata_2022-04.parquet` of the New York taxi trip [dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) and place it on a specific folder.

# Components
The application follows a micro-service approach with three services, namely an IoT car workload generator, an Edge server, and a Cloud server. 
The following image highlights the service graph and `yaml` docker-compose representation of the application.

<p align="center">
   <img width="500" src="../assets/images/car-application.png" alt="Car Application">
</p>

## IoT Data Generator

The IoT Data Generator reads the New York taxi trips file, and periodically sends several data points to a specific Edge server.
Users have to define environmental variables, including `TARGET_EDGE`, which is the IP or hostname of the target Edge server, `IOT_DATA_SIZE`, which is the number of rows that the service will disseminate, and `IOT_DATA_GENERATION_PERIODICITY` that specifies the periodicity in seconds.

## Edge Server

The Edge server receives the data points of the IoT data generators via an HTTP API call, aggregates them, and temporarily stores them. 
Moreover, Cloud periodically requests Edge servers, and when the Edge component serves its aggregated data, removes and initializes them.

## Cloud Server

Cloud server retrieves the aggregated data from the Edge devices in specific period durations. 
Users should set an environmental variable `EDGE_SERVERS` that is a comma-separated list of edge servers' IPs or hostnames.
Moreover, `COMPUTE_PERIODICITY` defines the periodicity of aggregated data retrieval and computation of final results. 
These results are stored in Cloud storage, and users can retrieve them via `GET` `HTTP` requests at the `/` path. 

# Build Application Components

In order for users to build the containers of the application, they need to execute the docker `build` command on very component's folder.

```bash
docker build -t workload-exp:0.0.1 .

docker build -t edge-exp:0.0.1 .

docker build -t cloud-exp:0.0.1 .
```
We also provide a `build-image.sh` file in every component's folder that users can execute to build their images.

```bash
bash ./build-image.sh
```

# Run the application via Docker-compose

Then, users should pass the dataset folder to the workload container `/data` folder.
For instance, the following part of the `docker-compose.yaml` injects `/home/ubuntu/data` to the `/data` folder of the container (`car` service).
```yaml
  car:
    environment:
      TARGET_EDGE: edge-two
      IOT_DATA_SIZE: 1
      IOT_DATA_GENERATION_PERIODICITY: 5
    image: workload-exp:0.0.1
    volumes:
      - /home/ubuntu/data:/data
    networks:
      - internet
```



