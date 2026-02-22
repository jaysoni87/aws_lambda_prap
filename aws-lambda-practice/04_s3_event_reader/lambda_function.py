def lambda_handler(event, context):
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']

        print(f"File {file_name} uploaded to {bucket_name}")

        return {
            "statusCode": 200,
            "message": f"{file_name} processed successfully"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }