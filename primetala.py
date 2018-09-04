n = int(input("Input a natural number: ")) # Do not change this line

import math
i = 2
prime = True

while i <= int(math.sqrt(n)):
    if n % i == 0:
        prime = False
        break
    
    i = i + 1

if prime:
     print("Prime")
else:
    print("!Prime")        