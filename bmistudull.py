weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line
height_float = (float(height_str) / 100)

weight_float = float(weight_str)
bmi = (weight_float / (height_float)**2)
print("BMI is: ", bmi) # do not change this line









#BMI is a number calculated from a person's weight and height.  The formula for BMI is:
#weight / height2
#where weight is in kilograms and heights is in meters
#Write a program  that prompts for weight in kilograms and height in centimeters and outputs the BMI.