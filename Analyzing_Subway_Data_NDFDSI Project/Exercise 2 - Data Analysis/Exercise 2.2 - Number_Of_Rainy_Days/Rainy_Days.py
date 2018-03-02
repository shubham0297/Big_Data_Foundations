
'''
Exercise 2.2			NUMBER OF RAINY DAYS

Problem Statement :

Now, create a function that calculates the number of rainy days. For this, return the count of the number of days where the column "rain" is equal to 1.

Tip: You might think that interpreting numbers as integers or floats might not work at first. To handle this issue, it might be useful to convert these numbers into integers. You can do this by writting cast (column as integer). So, for example, if we want to launch the column maxtempi as an integer, we have to write something like cast (maxtempi as integer) = 76, instead of just where maxtempi = 76.
'''




#Solution :

import pandas as pd

filename = "turnstile_data_master_with_weather.csv"		# Point 1	
df = pd.read_csv(filename);

def num_rainy_days(df):

    count = df['rain'].astype(int).sum()   				# Point 2  
    return count

print(num_rainy_days(df))								# Point 3

'''
KEY POINTS

1. 	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Rainy_Days.py) IS
2.	astype(int) is used to convert column values to int ....and sum function is used to calculate the number of rainy days
3.	num_rainy_days(df) calls the function and since the function returns the count of number of day, print(num_rainy_days(df)) prints the count
'''    