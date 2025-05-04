# print ("Hello world")
first_name = "Hamza"
#print(type (first_name)==str)
age= input ("enter your age:")
#age = int (age)
# if type (age)==str:
    #print("invalid input")
#Below is the correct code

if age.isdigit():
    print(age)
else:
    print("Invalid input")
