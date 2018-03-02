'''
Exercise 2.6				HISTOGRAMS FOR ENTRIESn_hourly

Problem Statement :

Before you make any analysis, it might be useful to look at the data we want to analyse. More specifically, we will evaluate the entries by hour in our data from the NYC Subway to determine the data distribution. This data is stored in the column ['ENTRIESn_hourly'].

Draw two histogramns in the same axis, to show the entries when it's raining vs when it's not. Below, you will find an example of how to draw histogramns with Pandas and Matplotlib:

Turnstile_weather ['column_to_graph']. Hist ()
'''




#Solution :

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "turnstile_data_master_with_weather.csv"		# Point 1	
df = pd.read_csv(filename);

def entries_histogram(turnstile_weather):
    
    plt.figure()
    plt.title("Histogram showing ENTRIESn_hourly")
    turnstile_weather.loc[turnstile_weather['rain']==1]['ENTRIESn_hourly'].hist(bins=20,histtype='bar',rwidth=0.95,color='Purple',label='Rainy Day') 	# Point 2 
    turnstile_weather.loc[turnstile_weather['rain']==0]['ENTRIESn_hourly'].hist(bins=20,histtype='bar',rwidth=0.95,color='Cyan',label='Normal Day') 	# Point 3
    plt.legend()
    return plt

entries_histogram(df).show()							# Point 4


'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Histogram.py) IS.
2.  Code to plot a historgram for hourly entries when it is raining
3.	Code to plot a historgram for hourly entries when it is not raining
4.	entries_histogram(df).show() calls the function and since the function plots the histogram of ENTRIESn_hourly for rainy and non-rainy day,
	(avg_min_temperature(df).show() shows the plotted histogram.
'''
