secs_str = int(input("Input seconds: ")) # do not change this line
hours = int(secs_str // 3600) # hours =
secs_str = secs_str - hours * 3600

minutes = int(secs_str // 60)
secs_str = secs_str % 60
seconds = secs_str
print(hours,".", minutes, "," , seconds)
