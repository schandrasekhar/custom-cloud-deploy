import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input


def create_instance_template(compute, project, name):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='debian-cloud', family='debian-8').execute()
    source_disk_image = image_response['selfLink']
    instance_template_body = {
        'name': name,
        'properties': {
            'machineType': 'n1-standard-1',
            'disks': [{
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }],
            # Specify a network interface with NAT to access the public
            # internet.
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [
                    {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
                ]
            }],

            'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],
        }
    }
    # TODO: Add desired entries to the request body.

    return compute.instanceTemplates().insert(
        project=project, 
        body=instance_template_body).execute()

def delete_instance_template(compute, project, name):
    return compute.instanceTemplates().delete(
        project=project,
        instanceTemplate=name).execute()

# [START list_instances]
def list_instance_templates(compute, project):
    result = compute.instanceTemplates().list(project=project).execute()
    return result['items']
# [END list_instances]