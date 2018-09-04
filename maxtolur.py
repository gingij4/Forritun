num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line
biggest = int(num1)

if num2 < num1 > num3:
    biggest = num1
if num1 < num2 > num3:
    biggest = num2
if num1 < num3 > num2:
    biggest = num3

print("The maximum is: ", biggest) # Do not change this line

#Write a program that reads in 3 integers and prints out the maximum of the three