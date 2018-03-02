'''
Exercise 2.5			MEAN OF MINIMUM TEMPERATURE 

Problem Statement :

Calculate the mean of the minimum temperature 'mintempi' for the days when the minimum temperature was greater that 55 degrees:
'''




#Solution :

import pandas as pd

filename = "turnstile_data_master_with_weather.csv"		# Point 1	
df = pd.read_csv(filename);

def avg_min_temperature(filename):

    filename = filename.loc[filename['mintempi']>55]    # Point 2 
    avg_min_temp_rainy = filename['mintempi'].mean()   	# Point 3  
    
    return avg_min_temp_rainy

print(avg_min_temperature(df))							# Point 4





'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Mean_Of_Min_Temperature.py) IS.
2.	Filters the dataframe and gives only the rows with 'mintempi'>55 degrees.
3.	.mean()	---->	calculates the means of the filtered dataframe.
4. 	avg_min_temperature(df) calls the function and since the function returns the average of minimun temperature,
	print(avg_min_temperature(df)) prints that average temperature.
'''