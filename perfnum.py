top_num = int(input("Upper number for the range: ")) # Do not change this line

for j in range(2,top_num+1):
    x = 0
    for i in range(j-1,0,-1):
        if j % i == 0:
            x +=i
            
    if x == j:
        print(x)        
        
   
