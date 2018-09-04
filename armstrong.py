top_num = int(input("Input a number between 0 and 999: "))
x = 0

for i in range(top_num):
    if i < 10:
        if (i**1) == i:
            print(i)
    if (100<=i) and (i<=999):
        num1 = i // 100
        num2 = ((i // 10)%10)
        num3 = i % 10        
        if ((num1**3)+(num2**3)+(num3**3))==i:
            print(i)
