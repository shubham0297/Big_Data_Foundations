'''
Exercise 2.4		MEAN TEMPERATURE ON WEEKENDS

Problem Statement :

Now, calculate the mean for 'meantempi' for the days that are Saturdays or Sundays (weekend):
'''




#Solution :

import pandas as pd

filename = "turnstile_data_master_with_weather.csv"		# Point 1	
df = pd.read_csv(filename);

def avg_weekend_temperature(filename):
  
    filename['DATEn']=pd.to_datetime(filename.DATEn)   	# Point 2 
    day=(filename.DATEn.dt.weekday).astype(int)  		# Point 3
    filename = filename.loc[ (day==5) | (day==6)]   	# Point 4
    mean_temp_weekends = filename['meantempi'].mean()   # Point 5
    return mean_temp_weekends

print(avg_weekend_temperature(df))						# Point 6




'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Mean_Temperature_On_Weekends.py) IS.
2. 	pd.to_datetime(column_name) ---->	Convert datatype of DATEn column fron object to Datetime.
3.	dt.weekday ---->	retrieves the Day[0-6] from the given DATE where 0 is for Monday and  6 is for Sunday/
4.	Filters the dataframe and gives only the rows which have day='SATURDAY'(5) or 'SUNDAY'(6).
5.	.mean() ----> calculates the mean of 'meantempi' column from filtered dataframe
6.	avg_weekend_temperature(df) calls the function and since the function returns the average temperature on weekend ,
	print(avg_weekend_temperature(df)) prints that average temperature.
'''
    