years_str = input("Years: ") # do not change this line

years_int = int(years_str)
population_int = int(3073986362)
#sek í ári = 31536000
born_int = int(31536000 / 7)
dautt_int = int(31536000 / 13)
innflytjandi_int = int(31536000 / 35)
new_population = population_int + (born_int - dautt_int + innflytjandi_int) * years_int


print("New population after", years_int, " years is ", int(new_population)) # do not change this line




#Assume that the current US population is 307,357,870 and that these rates of change are provided:

#a birth every 7 seconds
#a death every 13 seconds
#a new immigrant every 35 seconds
#Write a program that takes years as input (as an integer) and prints 
#out an estimated population (as an integer).  Assume that there are exactly 365 days in a year.