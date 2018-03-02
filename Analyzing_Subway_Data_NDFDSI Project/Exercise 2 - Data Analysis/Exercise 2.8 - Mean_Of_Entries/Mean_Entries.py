'''
Exercise 2.8			MEAN ENTRIES ON RAINY AND NON RAINY DAY

Problem Statement :

Build a function that returns:

1.The mean of entries when it's raining
2.The mean of entries when it's not raining

Answer to the following questions according to your functions' exits:

a)	What is the mean of entries when it's raining?
b)	What is the mean of entries when it's not raining?
'''




#Solution :

import numpy as np

import pandas as pd

filename = "turnstile_data_master_with_weather.csv"						# Point 1	
df = pd.read_csv(filename);

def means(turnstile_weather):
    
    p=""  																# Point 2 
    rainy_days = turnstile_weather.loc[turnstile_weather['rain']==1]    # Point 3 
    normal_days = turnstile_weather.loc[turnstile_weather['rain']==0]   # Point 4 
    with_rain_mean = rainy_days['ENTRIESn_hourly'].mean();      		# Point 5 
    without_rain_mean = normal_days['ENTRIESn_hourly'].mean();  		# Point 6         
    
    return with_rain_mean, without_rain_mean, p 						# leave this line for the grader
	
print(means(df))														# Point 7


#	a) 		Mean of entries when it's raining = 1105.4463767458733
#	b)		Mean of entries when it's not raining = 1090.278780151855





'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Histogram.py) IS.
2.	Didn't understand what 'p' was in the return statement of question, so took it as empty string.
3.	Filters dataframe and gives data for only rainy days.
4.	Filter dataframe and gives only non-rainy days.
5.	Gives the means of 'ENTRIES's_hourly' column from filtered rainy_days dataframe.
6.	Gives the means of 'ENTRIES's_hourly' column from filtered normal_days dataframe.
7.	means(df) calls the function and since the function returns the mean of rainy days,mean of non-rainy days and one more thing,
	print(means(df)) prints those mean values.
'''