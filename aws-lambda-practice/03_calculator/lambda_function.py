def lambda_handler(event, context):
    a = event.get("a", 0)
    b = event.get("b", 0)
    operation = event.get("operation", "add")

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b if b != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"

    return {
        "statusCode": 200,
        "result": result
    }