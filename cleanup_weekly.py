import boto3
import datetime
# ---------------------Made by shalev pinker -----------------------------------------------------
# ---------------------
# -------------------- This script will check for unattached volumes, elastic ips, snapshots------------------

# Connect to AWS with default configuration in ~/.aws/config 
session = boto3.Session(profile_name='default2')
ec2 = session.resource('ec2',region_name='us-east-1')
#ec2 = boto3.resource('ec2',region_name='us-east-1')
#instance_id = 'i-0df7872e95d75b597'
count = 0
regions = ['ap-northeast-1', 'ap-southeast-1', 'eu-central-1', 'eu-west-1', 'sa-east-1', 'ap-southeast-2','us-east-1']
#regions = ['eu-west-1']

# This function will get the name of the volume with a given volume attribute
def name_of_volume(volume_tags):
	volume_name = ''
	#if ( != '')
	for tag in volume_tags:
		if (tag.get('Key') == 'Name'):
			volume_name = tag.get('Value')
	return volume_name

# This will return list of volume id that are AVAILABLE in a given region
def id_of_available_volume(region):
	ec2 = session.resource('ec2',region_name=region)
	list_to_return = []
	for volume in ec2.volumes.all():
		Thevolume = ec2.Volume(volume.volume_id)
		if ( Thevolume.state == 'available'):
			list_to_return.append(Thevolume.volume_id)
	return list_to_return

# Volume report for region
def report_of_volume(region):
	ec2 = session.resource('ec2',region_name=region)
	for x in id_of_available_volume(region):
        	volume = ec2.Volume(x)
		if (volume.tags == None):
			print "Volume id:  %s " %(x)
		elif (name_of_volume(volume.tags) == ''):
			 print "Volume id:  %s " %(x)

def report_of_elastic(region):
	client = session.client('ec2',region_name=region)
	addresses_dict = client.describe_addresses()
	for elastic_ip in addresses_dict.get('Addresses'):
        	if (elastic_ip.get('InstanceId') == None):
			print "Elastic IP : %s  has no instance attached " %(elastic_ip.get('PublicIp'))
#		print elastic_ip.get('InstanceId')

#report_of_elastic('eu-central-1')
# This will Generate report for every region
for region in regions:
	print "Report for region:%s \n" %(region)
	report_of_volume(region)
	report_of_elastic(region)

	
#import boto3
#client = boto3.client('ec2',region_name='eu-central-1')
#addresses_dict = client.describe_addresses()

#for elastic_ip in addresses_dict.get('Addresses'):
#	print elastic_ip.get('InstanceId')
#	print elastic_ip['InstanceId']
	#print elastic_ip['InstanceId']
#print addresses_dict.get('Addresses')[0]['InstanceId']

