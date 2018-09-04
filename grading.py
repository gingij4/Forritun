grade = float(input("Input a grade: ")) # Do not change this line

if grade < 0.0 or grade > 10.0:
    print("Invalid grade!") # Do not change this line
elif 5.0 <= grade <= 10.0:
    print("Passing grade!") # Do not change this line
elif 0.0 <= grade < 5.0:
    print("Failing grade!") # Do not change this line




#A passing grade is between 5.0 and 10.0 (both inclusive).  
# The program pints out "Invalid grade!", "Passing grade!", or "Failing grade!", depending on the input.