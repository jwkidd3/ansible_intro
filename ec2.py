#!/usr/bin/env python3
import boto3
import json

def get_aws_ec2_inventory():
    # Replace these variables with your AWS credentials and region
    aws_region = 'us-east-1'

    ec2 = boto3.client(
        'ec2',
        region_name=aws_region
    )

    # Filter EC2 instances based on your criteria
    #{'Name': f'tag:{tag_key}', 'Values': [tag_value]},
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
    {'Name': 'tag:role', 'Values': ['user25-web']}])
    ec2_instances = response['Reservations']

    return ec2_instances

def generate_inventory():
    ec2_instances = get_aws_ec2_inventory()

    inventory = {'all': {'hosts': []}, '_meta': {'hostvars': {}},'web': {'hosts': []}}

    for reservation in ec2_instances:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            private_ip = instance['PrivateIpAddress']
            public_ip = instance.get('PublicIpAddress', 'N/A')

            inventory['all']['hosts'].append(instance_id)
            inventory['web']['hosts'].append(instance_id)
            inventory['_meta']['hostvars'][instance_id] = {
                'ansible_host': private_ip,
                'public_ip': public_ip,
            }

    print(json.dumps(inventory))

if __name__ == '__main__':
    generate_inventory()
