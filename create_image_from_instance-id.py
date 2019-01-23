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

# This function will get instance name from a given instance id
def get_image_name(instance_id):
	instance_name= ''
	instance = ec2.Instance(str(instance_id))
	for tag in instance.tags:
		if (tag.get('Key') == 'Name'):
			instance_name = tag.get('Value')
	return instance_name

# This function will create an image from a given instance_id
# Name Format ---------- instance_name+month-day-year
def create_image(instance_id):
	instance = ec2.Instance(str(instance_id))
	client = boto3.client('ec2',region_name='us-east-1')
	client.create_image(
		Description='image from instance ' + get_image_name(instance_id),
		InstanceId=str(instance_id),
		Name=get_image_name(instance_id)+datetime.date.today().strftime("%B %d, %Y").replace(" ","-").replace(",",""),
		NoReboot=True
)

#create_image(instance_id)

