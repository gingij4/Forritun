secs_str = int(input("Input seconds: ")) # do not change this line
hours = (secs_str // 3600) # hours =
minutes = hours % secs_str
seconds = minutes % 60
print(hours,".", minutes, "," , seconds)