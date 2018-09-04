n = int(input("Input an int: ")) # Do not change this line

counter = 1


while counter <= n:
    if n % counter == 0:
        print(counter)
    counter += 1        

