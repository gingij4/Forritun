i = 9
while i < 1000:
    i = i + 1
    t = i**2
    if i == t % 100:
        print (i)
        break