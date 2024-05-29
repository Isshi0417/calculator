import json

LANGUAGE = 'jp'

with open('message.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang):
    return MESSAGES[lang][message]

def prompt(key):
    message = messages(key, LANGUAGE)
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('welcome')


# keep repeating
while True:
    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('operations')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('invalid_operation')
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    if (LANGUAGE == "en"):
        print(f'=> The result is {output}')
    else:
        print(f'=> 合計は{output}です')
    
    # ask again
    prompt("another_one")
    answer = input().lower()
    if (answer and answer[0] != "y") or answer == "":
        break