import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')


def list_instances():
    instances_data = []
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                volumes = ec2.describe_volumes(
                    Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}]
                )
                volume_data = [{
                    'VolumeId': v['VolumeId'],
                    'Size': v['Size'],
                    'State': v['State']
                } for v in volumes['Volumes']]

                attrs = ec2.describe_instance_attribute(InstanceId=instance_id, Attribute='disableApiStop')
                stop_protection = attrs['DisableApiStop']['Value']
                attrs = ec2.describe_instance_attribute(InstanceId=instance_id, Attribute='disableApiTermination')
                termination_protection = attrs['DisableApiTermination']['Value']

                instances_data.append({
                    'instance_id': instance_id,
                    'state': instance['State']['Name'],
                    'stop_protection': stop_protection,
                    'termination_protection': termination_protection,
                    'volumes': volume_data,
                    'security_groups': instance['SecurityGroups']
                })
        return instances_data
    except ClientError as e:
        raise RuntimeError(f"AWS error: {e}")


def modify_volume_size(volume_id, new_size):
    try:
        ec2.modify_volume(VolumeId=volume_id, Size=new_size)
        return True
    except ClientError as e:
        raise RuntimeError(f"Failed to modify volume: {e}")


def set_protection(instance_id, stop, termination):
    try:
        ec2.modify_instance_attribute(InstanceId=instance_id, DisableApiStop={'Value': stop})
        ec2.modify_instance_attribute(InstanceId=instance_id, DisableApiTermination={'Value': termination})
    except ClientError as e:
        raise RuntimeError(f"Protection setting error: {e}")


def manage_security_rule(rule):
    try:
        ip_permission = {
            'IpProtocol': rule['protocol'],
            'FromPort': rule['from_port'],
            'ToPort': rule['to_port'],
            'IpRanges': [{'CidrIp': rule['cidr_ip']}]
        }

        if rule['direction'] == 'inbound':
            if rule['action'] == 'add':
                ec2.authorize_security_group_ingress(GroupId=rule['group_id'], IpPermissions=[ip_permission])
            else:
                ec2.revoke_security_group_ingress(GroupId=rule['group_id'], IpPermissions=[ip_permission])
        elif rule['direction'] == 'outbound':
            if rule['action'] == 'add':
                ec2.authorize_security_group_egress(GroupId=rule['group_id'], IpPermissions=[ip_permission])
            else:
                ec2.revoke_security_group_egress(GroupId=rule['group_id'], IpPermissions=[ip_permission])
    except ClientError as e:
        raise RuntimeError(f"Security group rule error: {e}")

