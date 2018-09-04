d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if 1 <= d1 <= 6 and 1 <= d2 <= 6:
    sum = d1 + d2
    if 7 <= sum <= 11:
        print("Winner")  
    elif sum in [2,3,12]:
        print("Loser")
    else:
        print(sum)

else:   
     print("Invalid input")

  




# Fill in the missing code below
#Accept d1 and d2, the number on two dices as input. First, 
# check to see that they are in the proper range for dice (1-6). 
# If not, print the message "Invalid input". Otherwise, determine the sum.
#  If the sum is 7 or 11, print "Winner". If the sum is 2, 3 or 12, print "Loser". Otherwise print the sum.