# A Dummy 3-tier IoT Application Template

This a template for a 3-tier IoT application that includes a workload generator, an Edge server, and a Cloud server.
The workload generator is responsible to reproduce a dataset that the user provides with a base periodicity 
and sends IoT data points to a specific Edge Server instance. 
Then, the Edge servers aggregate the incoming region-based IoT data points and store them. 
Finally, the Cloud server periodically requests all Edge nodes to retrieve their partially generated data and produces the final results.
Moreover, the Cloud server exposes the results via an HTTP request (a `GET` request at `/`).

In the `.py` files, we provide specific instructions (via `TODO` comments) on what type of code and actions should be provided.  
Moreover, an already implemented application is the `taxi-app-example` that can be found in the root repository. 