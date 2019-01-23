#!/usr/bin/env python
import boto3
import datetime


# ---------------------Made by shalev pinker -----------------------------------------------------
# ---------------------
# -------------------- This script will modify/create topic in sns------------------

# Connect to AWS with default configuration in ~/.aws/config 
session = boto3.Session(profile_name='default')
sns = boto3.resource('sns',region_name='us-east-1')
subscription = sns.Subscription('arn')
client = boto3.client('sns',region_name='us-east-1')

# This function will add subscribers to a given topic
def add_subscriber_topic(str_topic,str_subscriber):
	response = client.subscribe(
    		TopicArn=topic_arn(str_topic),
    		Protocol='email',
    		Endpoint=str_subscriber
	)


# This will give you arn of an topic by name
def topic_arn(str_topic_name):
	response = client.list_topics()
	for topic in response['Topics']:
		if (topic['TopicArn'].endswith(str_topic_name)):
			return topic['TopicArn']
# This will create a topic
def create_topic(name_of_topic):
	response = client.create_topic(
    	Name=name_of_topic
	)

#response = client.list_topics()
add_subscriber_topic('new_topic','shalevking4@walla.co.il')

#print response['Topics'][0]['TopicArn']

#create_topic("new_topic")





