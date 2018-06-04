## Custom Cloud Deploy `ccd`
This is a custom cloud deployment and orchestration solution for google cloud(as of now). Once the architecture and the implementation is more concrete and modular, I will try to port it to another cloud infrastructure like AWS. I recently needed to build apps, deploy and maintain them. Some of the apps were critical in terms of downtime, security and reliability so I needed some sort of an automated way of deploying and maintaining them to ensure little to no downtime. I could have used something like Kubernetes but decided against it for a couple of reasons. Firstly it involves a learning curve (which might not be a bad thing). Secondly wanted to see if I can build a simple cloud deployment and orchestration framework for my needs. Hopefully this will not become a nightmare and will lead to something interesting and useful.

***

#### What are the basic requirements of an application
1. a machine to execute its code securely
2. a uniform and secure way to communicate with dependent applications(clients or servers or downstream systems)
3. a place to securely store and securely access in a uniform way its data(consumer data or it's own data)
4. a way to autoscale itself with customer demand
5. should be highly available


#### Implementation details of the above requirements
##### 1.
- Implemetation details
    - the application will run on a application container(say docker) which will run on a group of virtual machines as a 1:1 pair
        - in gcloud it will be instance group, with application specific disk, image, instance template configurations respectively
        - a deployment service will be provided which will create a application container with all the dependencies and deploy to the respective instance group 

##### 2.
- Implementation details
    - for external consumers a load balancer will provide encrypted communication
        - will done via a `https` connection
        - various firewalls will be in place to make the application secure
    - for internal applications only internal ip restrictions will be provided
        - will be done via internal ip address spaces
        - various firewalls will be in place to make the application secure

##### 3.
- Implementation details
    - a highly available persistent database service with authentication management will be provided to store data blobs
        - the application will have a user account in the database service
        - sql and nosql databases will be provided
    - a highly available non persistent database service will be provided to store data blobs in a non persistent way
        - a cache service in redis will be provided
        - the keys in this cache will be prefixed with the application namespace
        - no authentication or authorization will be provided in this case
    - a highly available persistent file system storage will be provided for storing application files (say logs)
        - a log service will be provided which collects logs and sends them to the persistent file system storage
        - a service will be provided by which the application can store and view files in a persistent way

##### 4.
- Implementation details
    - a mechanism will be available to the application in an optional manner to scale itself in case of high load/traffic
        - a local service will run to check machine resource statictics and send alerts as needed
        - a alerts service will be available that can take actions(say autoscale) on alerts recieved


##### 5.
- Implementation details
    - a mechanism will be available to the application in an optional manner to restart itself in case of errors
        - a local service will be provided which will run preconfigured health checks and send alerts as needed
        - a alerts service will be available that can take actions(say kill and restart service) on alerts recieved
    - will be deployed as a cluster to have fail safe options
        - this will be handled by the deployment service
    - will follow various deployment statergies like hot-cold, on the fly via application configuration
        - this will be handled by the deployment service

***

### Architecture Overview
This repository will have various services which will be exposed to the developer and make it easier to deploy, maintain, scale and debug applications.

The core services can be defined as follows
- Deployment service
- Load balancer service
- Health check service
- Auto scale service


The third party services which make it easier to for application developers and which will be part of the `ccd` ecosystem are 
- Logging service
- Database services
- Cache services
- File system storage services


Each of the above defined services will be exposed to the developer to make use as he or she sees fit

***

### How to use this repository?
The above mentioned services will be exposed as API endpoints which can be accessed via REST.

***

### Repository structure
```
    /src/
        rest/
        models/
        dao/
            gcloud/
        services/
        config/
        scripts/
```

