#!/usr/bin/env python

# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example of using the Compute Engine API to create and delete instances.

Creates a new compute engine instance and uses it to apply a caption to
an image.

    https://cloud.google.com/compute/docs/tutorials/python-guide

For more information, see the README.md under /compute.
"""

import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input

import gcloudapis.compute.instance_template

from gcloudapis.compute.instance_template import create_instance_template
from gcloudapis.compute.instance_template import delete_instance_template
from gcloudapis.compute.instance_template import list_instance_templates
from gcloudapis.compute.instance_template import delete_instance_template

from gcloudapis.compute.instance import create_instance
from gcloudapis.compute.instance import list_instances
from gcloudapis.compute.instance import delete_instance


from gcloudapis.compute.disk import create_disk
from gcloudapis.compute.disk import list_disks
from gcloudapis.compute.disk import delete_disk

from gcloudapis.compute.image import create_image
from gcloudapis.compute.image import list_images
from gcloudapis.compute.image import delete_image


# [START wait_for_operation]
def wait_for_zone_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)
# [END wait_for_operation]

def wait_for_global_operation(compute, project, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.globalOperations().get(
            project=project,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)



def instance(project, bucket, zone, instance_name, wait=True):
    compute = googleapiclient.discovery.build('compute', 'v1')

    print('Creating instance.')
    operation = create_instance(compute, project, zone, instance_name, bucket)
    wait_for_zone_operation(compute, project, zone, operation['name'])

    instances = list_instances(compute, project, zone)

    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        print(' - ' + instance['name'])

    print("""
Instance created.
It will take a minute or two for the instance to complete work.
Check this URL: http://storage.googleapis.com/{}/output.png
Once the image is uploaded press enter to delete the instance.
""".format(bucket))

    if wait:
        input()

    print('Deleting instance.')

    operation = delete_instance(compute, project, zone, instance_name)
    wait_for_zone_operation(compute, project, zone, operation['name'])





def instance_template(project, instance_name, wait=True):
    compute = googleapiclient.discovery.build('compute', 'v1')
    print('Creating instance template')
    operation = create_instance_template(compute, project, instance_name)

    wait_for_global_operation(compute, project, operation['name'])
    instances = list_instance_templates(compute, project)


    print('Instances in project %s:' % (project))
    for instance in instances:
        print(' - ' + instance['name'])

    print("""
Instance created.
It will take a minute or two for the instance to complete work.
Once the image is uploaded press enter to delete the instance.
""")

    if wait:
        input()

    print('Deleting instance.')

    operation = delete_instance_template(compute, project, instance_name)
    wait_for_global_operation(compute, project, operation['name'])



def disk(project, zone, instance_name, wait):
    compute = googleapiclient.discovery.build('compute', 'v1')
    print('Creating disk')
    operation = create_disk(compute, project, zone, instance_name)

    wait_for_zone_operation(compute, project, zone, operation['name'])

    instances = list_disks(compute, project, zone)

    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        print(' - ' + instance['name'])

    print("""
Instance created.
It will take a minute or two for the instance to complete work.
Once the image is uploaded press enter to delete the instance.
""")

    if wait:
        input()

    print('Deleting disk.')

    operation = delete_disk(compute, project, zone, instance_name)
    wait_for_zone_operation(compute, project, zone, operation['name'])


def image(project, instance_name, wait):
    compute = googleapiclient.discovery.build('compute', 'v1')
    print('Creating image')
    operation = create_image(compute, project, instance_name)

    wait_for_global_operation(compute, project, operation['name'])

    instances = list_images(compute, project, zone)

    print('Images in project %s:' % (project))
    for instance in instances:
        print(' - ' + instance['name'])

    print("""
Instance created.
It will take a minute or two for the instance to complete work.
Once the image is uploaded press enter to delete the instance.
""")

    if wait:
        input()

    print('Deleting image.')

    operation = delete_image(compute, project, instance_name)
    wait_for_global_operation(compute, project, operation['name'])






# [START run]
def main(project, bucket, zone, instance_name, wait=True):
    # instance(project, bucket, zone, instance_name, wait)
    # instance_template(project, instance_name, wait)
    # disk(project, zone, instance_name, wait)
    image(project, instance_name, wait)





if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument(
        'bucket_name', help='Your Google Cloud Storage bucket name.')
    parser.add_argument(
        '--zone',
        default='us-central1-f',
        help='Compute Engine zone to deploy to.')
    parser.add_argument(
        '--name', default='demo-instance', help='New instance name.')

    args = parser.parse_args()

    main(args.project_id, args.bucket_name, args.zone, args.name)
# [END run]
