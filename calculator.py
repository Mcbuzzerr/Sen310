import json

def lambda_handler(event, context):
    operation = event["operation"]
    operand1 = event["operand1"]
    operand2 = event["operand2"]

    response = {}

    match operation:
        case "add":
            response["value"] = add(operand1, operand2)
        case "sub":
            response["value"] = sub(operand1, operand2)
        case "mul":
            response["value"] = mul(operand1, operand2)
        case "div":
            response["value"] = div(operand1, operand2)
        case default:
            raise ValueError(f"Invalid operation {operation}")
        
    return response

def add(x, y):
    return x+y
 
def sub(x, y):
    return x-y
 
def mul(x, y):
    return x * y
 
def div(x, y):
    return x/y


if __name__ == "__main__":
    event = {
        "operation": "add",
        "operand1": 1,
        "operand2": 2
    }
    print(lambda_handler(event, None))