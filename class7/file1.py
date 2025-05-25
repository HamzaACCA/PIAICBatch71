# def fn1 (func2):
#     print ("Inside of fn1: hello")
#     func2()
# def fn2():
#     print("inside of fn2: world")
# fn1 (fn2)


# def auth_checker(fn):
#     def wrapper():
#         print("checking...")
#         fn()
#     return wrapper

# @auth_checker
# def access_dashboard():
#     print ("Open Portal")

# @auth_checker
# def get_addminssion():
#     print("Open Portal")

# access_dashboard()
# get_addminssion()

# names_of_students = ("Ali", "Hamza", "Hussain", "Tahir")
# count = 1
# for name in names_of_students:
#     print (f"S.No {count}. {name}")
#     count += 1

for num in range (1,100, 3):
    print(num)

# root_list = [num**2 for num in range (1,11) if num % 2 == 0]
# print (root_list)

import random
secret_number= random.randint(1,100)
while True:
    my_num= int{input("Guess the number:")}
    if my_num < secret_number:
        print ("Your number is too High")
    elif my_num > secret_number:
        print ("Your number is too Low")
    else:
        print ("You Won")
    break            


    




