stars = int(input("Max number of stars: ")) # Do not change this line
star = "*"
for i in range(1,stars):
    print(star*i)
for i in range(stars,0,-1):
    print(star*i)