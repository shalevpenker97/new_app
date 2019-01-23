#!/usr/bin/env python

import boto3
import datetime
# ---------------------Made by shalev pinker ------------------------------------------------------------
# ---------------------
# -------------------- This script will chcek for users with Attached directly policies------------------
# -------------------- it will display every user with number of attached policies ----------------------

# Connect to AWS with default configuration in ~/.aws/config 
session = boto3.Session(profile_name='default')
iam = boto3.resource('iam')
client = boto3.client('iam')


# This function will return number of attached policies to a given username
def number_of_policies(username):
	count =0
	user = iam.User(username)
	policies = user.attached_policies.all()
	# Check if there is a policy attached to the user
	for policy in policies:
	        if (policy != '' ):
         	       count+=1
	return count

# Run for each user and check
for user in client.list_users()['Users']:
	username = user['UserName']
	policy_number = number_of_policies(username)
	if policy_number > 0:
	       print "user %s has %s attached policies " %(username, str(policy_number))
	else:
	       print "user %s dosent have any policies attached" %(username)





