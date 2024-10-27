import boto3

#variable to access boto3 s3 client  methods
s3_client = boto3.client("s3")

#variable to access boto3 dynamodb resource  methods
dynamodb = boto3.resource("dynamodb")

#add dynamodb table name
db_table=dynamodb.Table("employee-dev")

def lambda_handler(event, context):
	#fetch bucket name
	bn = event['Records'][0]['s3']['bucket']['name']
	#fetch file from s3 bucket
	file_name= event['Records'][0]['s3']['object']['key']
	#using get_object functin to fetch bucket and file from s3
	a = s3_client.get_object(Bucket=bn,Key=file_name)
	#decode and return value as string
	b = a['Body'].read().decode("utf-8")
	#split string into list(each word as list)
	c = b.split("\n")
	for d in c:
		e=d.split(",")
		db_table.put_item(
			Item=
			{
				"emp_id":e[0],
				"first_name":e[1],
				"last_name":e[2],
				"email":e[3]

			}
		)
	return 'Completed'