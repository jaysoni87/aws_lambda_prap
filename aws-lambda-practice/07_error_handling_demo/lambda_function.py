def lambda_handler(event, context):
    try:
        number = event["number"]
        result = 100 / number

        return {
            "statusCode": 200,
            "result": result
        }

    except ZeroDivisionError:
        return {
            "statusCode": 400,
            "error": "Division by zero is not allowed"
        }

    except KeyError:
        return {
            "statusCode": 400,
            "error": "Missing 'number' in input"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }