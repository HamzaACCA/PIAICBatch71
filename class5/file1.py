# def greet():
#     print("Hello World")
# greet()
# greet()

# def sum():
#     print(2+2)

# sum()

# def add():
#     print(2+2)
# add()    



# def calculator():
#     while True:
#         user_input = input("Enter calculation (e.g., '5 + 3' or '10 / 2'): ").strip()
#         parts = user_input.split()
        
#         # Check if we have exactly 3 parts (number op number)
#         if len(parts) != 3:
#             print("Error: Please enter in the format 'number operator number'")
#             continue
            
#         a_str, op, b_str = parts
        
#         # Validate first number
#         try:
#             a = float(a_str)
#         except ValueError:
#             print(f"Error: '{a_str}' is not a valid number")
#             continue
            
#         # Validate operator
#         if op not in {'+', '-', '*', '/'}:
#             print(f"Error: '{op}' is not a valid operator (use +, -, *, /)")
#             continue
            
#         # Validate second number
#         try:
#             b = float(b_str)
#         except ValueError:
#             print(f"Error: '{b_str}' is not a valid number")
#             continue
            
#         # Special case for division by zero
#         if op == '/' and b == 0:
#             print("Error: Cannot divide by zero")
#             continue
            
#         # All inputs valid - perform calculation
#         if op == '+':
#             result = a + b
#         elif op == '-':
#             result = a - b
#         elif op == '*':
#             result = a * b
#         elif op == '/':
#             result = a / b
            
#         print(f"Result: {result}")
#         break

# calculator()


# def calculator (num1, num2, operator):
#     if operator == '+':
#         print (num1 + num2)
#     elif operator == '-':
#         print (num1 - num2)
#     elif operator == '*':
#         print (num1 * num2)
#     elif operator == '/':
#         print (num1 / num2)
#     else:
#         print ("invalid input")

# num1=int(input ('Enter your first number:'))
# operator=input('Enter your operator(+, -, *, /):')
# num2=int(input('Enter your second number:'))

# calculator(num1 , num2, operator)


# def greet(age, name = "User"):
#     print(f'Hello {name} and you are {age} years old')
# greet(name='Hamza', age='15')


def calculator (num1, num2, operator):
    operator = '+'
    print(num1 + num2)
    return num1 + num2
output = calculator(1, 2, '+')

print (output)
