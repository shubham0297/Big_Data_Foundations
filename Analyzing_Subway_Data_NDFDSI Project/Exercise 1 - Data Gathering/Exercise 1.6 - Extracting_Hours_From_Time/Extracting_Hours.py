'''
Exercise 1.6				EXTRACTING HOURS FROM TIME

Problem Statement :

Given an entry variable that represents time, in the format: "00:00:00" (hour: minutes: seconds)

Write a function to extract the hour part from the time in the entry variable And return it as an integer. For example:

     1) if hour is 00, your code must return 0
     2) if hour is 01, your code must return 1
     3) if hour is 21, your code must return 21
Please return te hour as an integer.	
'''




#Solution :

import pandas

input_dataframe = pandas.read_csv("output_file.txt");					# Point 1

def time_to_hour(time):
    
    hour = time.TIMEn.str.slice(-8,-6).astype(int)   					# Point 2
    return hour

output_dataframe = time_to_hour(input_dataframe)					
output_dataframe.to_csv("output_file.txt",index=None)					# Point 3



'''
KEY POINTS

1.  NOTE ----> 'output.txt' is the output file of Exercise 1.5 . IT MUST BE PRESENT IN THE SAME FOLDER IN WHICH  this code(Extracting_Hours.py) is.
2.	Extractes just the hour part from TIMEn and converts it into integer.
	NOTE ----> IF YOU WANT TO ADD A SEPARATE NEW COLUMN IN EXISTING DATAFRAME THEN WRITE THE FOLLOWING CODE THEN CHANGE THE FUNCTION DEFINITION AS
	def time_to_hour(time):
		time['Hour_only'] = time['TIMEn'].str.slice(-8,-6).astype(int)   					
    		return time
3.	Writing back the returned dataframe (output_dataframe) to "output_file.txt". 	The output.txt for our code will contain ONLY the hour part of the TIMEn column
	If you want the output.txt to contain all the columns as and not just the hour part , change the function definition as given in KEY POINTS 2 
	If we don't write index=None , an extra column will be added to output file showing row index 
	Note ----> Now the 'output.txt' of Exercise 1.5 will be overwritten by the 'output.txt' created in point 3 .
'''
