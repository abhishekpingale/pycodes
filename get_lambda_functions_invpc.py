#-------------------------------------------------------------------------------
# Name: List Lambda Functions in VPC
# Purpose: To get the List of the Lambda Functions present in a VPC
#
# Version:     1.0
# Created:     05/07/2020
#-------------------------------------------------------------------------------

import boto3
from botocore.exceptions import ClientError

regions = ['ap-northeast-1', 'ap-southeast-1','ca-central-1', 'us-east-1', 'us-east-2']

for region_val in regions:
    session = boto3.session.Session()
    client = session.client(service_name='lambda', region_name=region_val)
    response = client.list_functions()
    result = response.get('Functions')
    if result:
        print("Checking Lambda Functions in Region :",region_val)
        inVPC=0
        notInVPC=0
        for lambda_func in result:
            if "VpcConfig" in lambda_func.keys():
                vpcConfig = lambda_func.get('VpcConfig')
                if vpcConfig['VpcId']:
                    inVPC+=1
                    # print("This is vpcConfig",vpcConfig)
                    print(f"Function: {lambda_func['FunctionName']} and VPC: {vpcConfig['VpcId']}")
            else:
                notInVPC+=1
                print(f"Function: {lambda_func['FunctionName']} Not in Vpc")
        print("Total Number of Lambda Functions in AWS Region is :", len(result))
        print(f"Number of Lambda Functions in VPC : {inVPC} and Number of Lambda Functions not in VPC : {notInVPC} for Region : {region_val}")
    else:
        print(f"No Lambda Function Present in Region : {region_val}")