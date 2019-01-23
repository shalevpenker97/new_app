#!/usr/bin/env python

import boto3
import datetime
# ---------------------Made by shalev pinker -----------------------------------------------------
# ---------------------
# -------------------- This script will create an image from a given instance_id------------------

# Connect to AWS with default configuration in ~/.aws/config 
session = boto3.Session(profile_name='default')
ec2 = boto3.resource('ec2',region_name='us-east-1')
instance_id = 'i-0df7872e95d75b597'

# This will create an instance in the same subnet of the instance that you choose
# PARAMETERS : ImageID , Name, KeyName, SecurityGroup
ec2.create_instances(
        ImageId='ami-030a7d008f399a01b',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='shalev_test_key',
        Monitoring={
        'Enabled': False
        },
        SecurityGroups=[
        'EC2-SG',
        ],
         Placement={
        'Tenancy': 'default'
        },
        TagSpecifications=[
        {
            'ResourceType':'instance',
                'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'This_is_new'
                },
            ],
        },
    ],
)

