#Create a converter that will ask for amount of days and convert it to years,
# then print it.
#Using int() function convert the user's answer to integer.
# And then make your calculation.
#You can ask something like:
# "How many days would you like to convert to a year?"

message=input("How many days would you like to convert to a year?")

# 365 days in a year 
result=float(message)/365


print(result)