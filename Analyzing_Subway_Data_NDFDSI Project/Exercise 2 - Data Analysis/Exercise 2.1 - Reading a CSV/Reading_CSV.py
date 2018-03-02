'''
Exercise 2.1		READING A CSV

Problem Statement : 

To understand the relationship between the Subway activity and the weather, please complete the data from the file already downloaded with the weather data. We provided you with the file containing NYC weather data and made it available with the Support Material. You can access it through the link: https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

Now that we have our data in a csv file, write Python code that reads this file and saves it into a Pandas Dataframe.

Tip:

Use the command below to read the file:

pd.read_csv('output_list.txt', sep=",")
'''




#Solution :

import pandas as pd

filename = "turnstile_data_master_with_weather.csv"
df = pd.read_csv(filename,sep=",")						# Point 1
	



'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file
'''