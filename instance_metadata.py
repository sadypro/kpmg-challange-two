import boto3
from itertools import islice
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-id","--instance_id",
                    help="Instance id of machine")
parser.add_argument("-key","--metadata_key",
                    help='''Enter Metadata key that you want to query , Refer 
                    These are the resource's available attributes:
Attribute='instanceType'|'kernel'|'ramdisk'|'userData'|'disableApiTermination'|'instanceInitiatedShutdownBehavior'|'rootDeviceName'|'blockDeviceMapping'|'productCodes'|'sourceDestCheck'|'groupSet'|'ebsOptimized'|'sriovNetSupport'|'enaSupport'|'enclaveOptions'|'disableApiStop' ''')
parser.add_argument("--profile",
                    help="AWS Profile name")
args = parser.parse_args()
id=args.instance_id
key=args.metadata_key
profile=args.profile
session = boto3.Session(profile_name=profile)
ec2 = session.client('ec2')
response = ec2.describe_instance_attribute(Attribute=key ,InstanceId=id)
t = list(response.items())
print(t[1])
