#Save Italy's GDP in a separate variable and remove it from the dictionary.

GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}


italy_gdp= GDP_2018.pop("Italy")


print(GDP_2018)
print(italy_gdp, "trillion USD")
