'''
Exercise 1.3             FILTERING THE DATAFRAME

Problem Statement:

For this exercise, you will write a function that reads the master_file created in the previous exercise and load it into a Pandas Dataframe. This function can be filtered, so that the Dataframe only has lines where column "DESCn" has the value "Regular".

For example, if the Pandas Dataframe looks like this:

,C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn
0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
1,A002,R051,02-00-00,05-01-11,04:00:00,DOOR,3144335,1088159
2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177
3,A002,R051,02-00-00,05-01-11,12:00:00,DOOR,3144424,1088231
The Dataframe must look like the following, after filtering only the lines where column DESCn has the value REGULAR:

0,A002,R051,02-00-00,05-01-11,00:00:00,REGULAR,3144312,1088151
2,A002,R051,02-00-00,05-01-11,08:00:00,REGULAR,3144353,1088177	
'''




#Solution:

import pandas

input_file = open("output_file.txt",'r')										#	Point 1
def filter_by_regular(filename):
    
    turnstile_data = pandas.read_csv("output_file.txt")
    turnstile_data = turnstile_data.loc[turnstile_data['DESCn']=='REGULAR'] 	# 	Point 2
																				
    return turnstile_data


df=filter_by_regular(input_file)												# 	Point 3
df.to_csv("output_file.txt",index=None)											# 	Point 4




'''
KEY POINTS

1.	NOTE ---->	'output.txt' is the output file of Exercise 1.2 . IT MUST BE PRESENT IN THE SAME FOLDER IN WHICH  this code(Filtering_Dataframe.py) is.
2.	dataframe.loc[condition]  method directly accesses specific locations of dataframe according to our req.For eg. in our example it will select rows have 'REGULAR' as the value of 'DESCn' column
3.	Function Calling part. We are passing the output_txt file from previous exercise ( which has merged data of 4 files) .
	Since function returns a filtered dataframe, df will contain the dataframe in which only entries which have DESCn='REGULAR' are present.
4.	Writing back the dataframe to "output_file.txt" which will be used in next exercise.  
	Note 1 ---->	 Now the 'output.txt' of Exercise 1.2 will be overwritten by the 'output.txt' created in point 4 . 
				 Now output.txt only has entries for which DESCn=REGULAR
	Note 2 ---->	 Check the output of output file if we remove index = None
'''