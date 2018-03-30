## Custom Cloud Deploy `ccd`
This is a custom cloud deployment and orchestration solution for google cloud(as of now). Once the architecture and the implementation is more concrete and modular, I will try to port it to another cloud infrastructure like AWS. I recently needed to build apps, deploy and maintain them. Some of the apps were critical in terms of downtime, security and reliability so I needed some sort of an automated way of deploying and maintaining them to ensure little to no downtime. I could have used something like Kubernetes but decided against it for a couple of reasons. Firstly it involves a learning curve (which might not be a bad thing). Secondly wanted to see if I can build a simple cloud deployment and orchestration framework for my needs. Hopefully this will not become a nightmare and will lead to something interesting and useful.

### Directory Structure
This repository contains the spefication of the components involved. I will try to be as verbose as possible. This will bring clarity as to what a component can and can't do. The spefication file will have the name of the component and will be written in markdown language. The code base for the components will be available on github and the repository names will be prefixed with `ccd`(Custom Cloud Deploy).

### Components
The components can be scripts (or/and) services the `ccd` framework provides and uses to provide deployment and orchestration functionality. The components are as follows:

#### machine-create-script
This component contains the set of scripts to create a instance template(google cloud), instance group(google cloud), presistent disks, firewall rules etc. This component contains all the necessary configurations to create a VM on the cloud infrastructure. Disk management, network sandboxing will also be handled by this script.

#### artifact-create-script
This component builds the package including all the dependencies.

#### deploy-app-script
This component deploys the respective application artifact to its respective virtual machine. This component will also handle hot cold deployments. Restarts if the virtual machine goes down.

#### machine-monitor-service
This monitors the health of the VM and does the required kill/restart operations.

#### process-monitor-service
This component monitors the health of the process. One can define various health checks for the process. If the health checks are not met the process is killed and restarted.

#### dns-service
This component has the ability to identify an application domain to its respective ip address group.

#### log-collect-service
This component collects the logs from various applications and stores them in a single place for future use.


## Deployment Use Cases
This framework will implement the following use cases

### Deploy application to cloud
TODO: create a xml workflow