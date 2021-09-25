def calculator(action, num1, num2):
    if action == 'multiply':
        return num1 * num2
    elif action == 'divide':
        return num1 // num2
    elif action == 'add':
        return num1 + num2
    elif action == 'subtract':
        return num1 - num2


operator = input()
number1 = int(input())
number2 = int(input())
print(calculator(operator, number1, number2))