## Custom Cloud Deploy `ccd`
This is a custom cloud deployment and orchestration solution for google cloud(as of now). Once the architecture and the code is more concrete and modular will try to port it to other cloud infrastructures like AWS. I recently had the need to build apps, deploy them and maintain them. Some of the apps were critical in terms of downtime, security and reliability so needed something an automated way of deploying apps and maintaining them to ensure little to no downtime. I could have used something like Kubernetes but decided against it for a couple of reasons. Firstly their is a learning curve (which might not be a bad thing), secondly wanted to see if I can build a simple cloud orchestration framework for my needs. Hopefully this will not become a nightmare and will lead to something interesting and will learn something useful of this project.

### Directory Structure
In this repository I will define the various parts of this framework and try to provide a spec for each of them. This will bring clarity as what a component's capabilities are. The spec file will have the name of the component and will be written in markdown language. The scripts for the various components will be available on github and the respective repositories will be prefixed with `ccd` as in Custom Cloud Deploy.

### Components
The components are as follows:

#### machine-create-script
This component contains the set of scripts to create a instance template(google cloud), instance group(google cloud), presistent disks, firewall rules etc. This component contains all the necessary configurations to create a VM on the cloud infrastructure. Disk management, network sandboxing will also be handled by this script.

#### artifact-create-script


