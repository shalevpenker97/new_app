#!/usr/bin/env python

import boto3
import datetime
# ---------------------Made by shalev pinker -----------------------------------------------------
# ------------------------------------------------------------------------------------------------
# -------------------- This script will upload/list/check files in s3------------------

# Connect to AWS with default configuration in ~/.aws/config 
session = boto3.Session(profile_name='default')
s3 = boto3.resource('s3')
client = boto3.client('s3')

# This will list objects in the given bucket
# Can  add Prefix to the returned object!!
def s3_list_new_objects(str_bucketname):
	response = client.list_objects(
	Bucket=str_bucketname
	)
	# Iterate over the objects in the bucket
	for document in response['Contents']:
		print "Document Name:%s LastModified:%s" %(document['Key'], document['LastModified'])
	

# This will upload files to a given s3 bucketname
def s3_upload_object(str_bucketname, str_file):
	s3.Bucket(str_bucketname).upload_file(str_file, 'hello.txt')
		
# This will download a specified file from a bucket to a uniqeplace in the system
def s3_download_file(str_buckername, str_remote_local_path, str_local_path):
	s3.meta.client.download_file(str_buckername, str_remote_local_path, str_local_path)	


#bucket_name = 'newtestingbucket4434'
#s3_list_new_objects(bucket_name)


#str_local_path = '/home/shalevpinker/Projects/FromBucket/new2.txt'

#str_remote_local_path = 'test_of_download_1'
#s3_download_file(bucket_name, str_remote_local_path, str_local_path)














