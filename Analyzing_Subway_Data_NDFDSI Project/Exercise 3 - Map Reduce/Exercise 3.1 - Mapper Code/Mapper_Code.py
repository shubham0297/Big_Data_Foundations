'''
Exercise 3.1			MAPPER CODE FOR UNIT AND ENTRIESn_hourly

Problem Statement :

The entry for this exercise is the same file from the previous session (Exercise 2). You can download the file from this link:

https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

Now, we will create a mapper. For each entry line, the mapper exit must PRINT (not return) UNIT as a key, and the number of ENTRIESn_hourly as the value. Separate the key and the value with a tab. For example: 'R002 \ t105105.0'

Export your mapper into a file named mapper_result.txt and send it with your submission. The code for exporting your mapper is already written in the code bellow.
'''




#Solution :

import sys

sys.stdin = open('turnstile_data_master_with_weather.csv')	 # Point 1
sys.stdout = open('mapper_result.txt', 'w')					 # Point 2


def mapper():
    sys.stdin.readline()          							 # Point 3
    for line in sys.stdin:
        data = line.strip().split(',')
        if len(data)==22:                                	 # Point 4 
           print ("{0}\t{1}".format(data[1],data[6]))    	 # Point 5
mapper()




'''
KEY POINTS

1.	Reads the turnstile_data_master_with_weather.csv file. 
	NOTE ---> "turnstile_data_master_with_weather.csv" MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Mapper.py) IS.
2.	Creates(Overwrites if already present) a file named 'mapper_result.txt' and writes the whatever is printed in sys.stdout in it.
3.  sys.std.readline() ----> reads the first line(Header Line) so it gets skipped. Otherwise it would have given undesired output.
4.	Ignore if any row has more or less than 22 columns. If condition will work only if we get 22 columns.
5.	data[1] is UNIT and data[6] is ENTRIESn_hourly. So we print them (in 'mapper_result.txt' ) with a tab ("\t") in between.	
'''