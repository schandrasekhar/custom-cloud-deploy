## Custom Cloud Deploy `ccd`
This is a custom cloud deployment and orchestration solution for google cloud(as of now). Once the architecture and the implementation is more concrete and modular, I will try to port it to another cloud infrastructure like AWS. I recently needed to build apps, deploy and maintain them. Some of the apps were critical in terms of downtime, security and reliability so I needed some sort of an automated way of deploying and maintaining them to ensure little to no downtime. I could have used something like Kubernetes but decided against it for a couple of reasons. Firstly it involves a learning curve (which might not be a bad thing). Secondly wanted to see if I can build a simple cloud deployment and orchestration framework for my needs. Hopefully this will not become a nightmare and will lead to something interesting and useful.