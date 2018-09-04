

n = int(input("Enter the length of the sequence: ")) # Do not change this line
einn = 0
tveir = 1
three = 0
for i in range(n):
    final = einn + tveir + three
    print(final)
    three = tveir
    tveir = einn
    einn = final
    