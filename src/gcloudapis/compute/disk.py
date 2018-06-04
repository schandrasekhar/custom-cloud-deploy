import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input


def create_disk(compute, project, zone, name):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='debian-cloud', family='debian-8').execute()
    source_disk_image = image_response['selfLink']

    config = {
        'name': name
    }

    return compute.disks().insert(
        project=project,
        zone=zone,
        body=config).execute()


def delete_disk(compute, project, zone, name):
    return compute.disks().delete(
        project=project,
        zone=zone,
        disk=name).execute()


def list_disks(compute, project, zone):
    result = compute.disks().list(project=project, zone=zone).execute()
    return result['items']
# [END list_instances]