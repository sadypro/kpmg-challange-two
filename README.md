# kpmg-challange-two
We need to write code that will query the meta data of an instance within AWS and provide a json formatted output. 

# Usage

* Login to AWS cli and take note of profile name 

* usage: instance_metadata.py [-h] [-id INSTANCE_ID]
                            [-key METADATA_KEY] [--profile PROFILE]    

* optional arguments:
<br />  -h, --help            show this help message and exit

<br />  -id INSTANCE_ID, --instance_id INSTANCE_ID     Instance id of machine
<br />  -key METADATA_KEY, --metadata_key METADATA_KEY
                        Enter Metadata key that you want to query ,    
                       
						Refer These are the resource's available       
                        attributes: Attribute='instanceType'|'kernel'  
                        |'ramdisk'|'userData'|'disableApiTermination'  
                        |'instanceInitiatedShutdownBehavior'|'rootDev  
                        iceName'|'blockDeviceMapping'|'productCodes'|  
                        'sourceDestCheck'|'groupSet'|'ebsOptimized'|'  
                        sriovNetSupport'|'enaSupport'|'enclaveOptions  
                        '|'disableApiStop'

<br />  --profile PROFILE     AWS Profile name
