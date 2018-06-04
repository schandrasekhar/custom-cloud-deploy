import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input


def create_image(compute, project, name):
    config = {
        'name': name
    }

    return compute.images().insert(
        project=project,
        body=config).execute()


def delete_image(compute, project, name):
    return compute.images().delete(
        project=project,
        disk=name).execute()


def list_images(compute, project):
    result = compute.images().list(project=project).execute()
    return result['items']
