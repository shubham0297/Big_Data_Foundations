'''
Exercise 2.3			MAXIMUM TEMPERATURE ON FOGGY DAY​

Problem Statement :

Calculate if the day was cloudy or not (0 or 1) and the maximum temperature for fog (i.e. the maximum temperature for cloudy days).
'''




#Solution :

import pandas as pd

filename = "turnstile_data_master_with_weather.csv"		# Point 1	
df = pd.read_csv(filename);

def max_temp_aggregate_by_fog(df):
    
    df = df.loc[df['fog']==1]    						# Point 2
    max_temp= df['maxtempi'].max()   					# Point 3
    return max_temp


print(max_temp_aggregate_by_fog(df))					# Point 4





'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Maximum_Temperature.py) IS.
2.	dataframe.loc[dataframe['fog']==1] ----> Filters the dataframe and gives only the rows which have value of fog=1.
3.	Gives  the maximum value of 'maxtempi' column amongst the filtered rows.
4.	max_temp_aggregate_by_fog(df) calls the function and since the function returns the maximum temperature on a foggy day,
	print(max_temp_aggregate_by_fog(df)) prints that maximum temperature.
'''
