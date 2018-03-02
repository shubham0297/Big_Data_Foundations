'''
Exercise 1.5			CREATING NEW COLUMN IN DATAFRAME (EXITSn_hourly)

Problem Statement :

Do the same thing you did in the previous exercise, but taking into account the exits, column EXITSn. For this, you need to create a column called EXITSn_hourly and insert the difference between the column EXITSn in the current line vs he previous line. If there is any NaN, fill it out/replace by 0.	
'''




#Solution :

import pandas

input_dataframe = pandas.read_csv("output_file.txt");					# Point 1

def get_hourly_exits(df):
    
    df['EXITSn_hourly']=df['EXITSn']-df['EXITSn'].shift(1)  			# Point 2
    df.fillna(value=0,inplace=True)                     				# Point 3 
    df.EXITSn_hourly = df.EXITSn_hourly.astype(int)  					# Point 4
    
    return df

output_dataframe = get_hourly_exits(input_dataframe)					
output_dataframe.to_csv("output_file.txt",index=None)					# Point 5



'''
KEY POINTS

1.	NOTE ---->	'output.txt' is the output file of Exercise 1.4 . IT MUST BE PRESENT IN THE SAME FOLDER IN WHICH  this code( New_Column(EXITSn_hourly).py	) is.
2.	This line adds a new column EXITSn_hourly and assigns to it the value of difference of EXITSn column of ith and i-1 row.
 	dataframe.shift(x) shifts the dataframe by x units.
3.	dataframe.fillna(value=x)  ----> fills the NAN values with x.
4.	dataframe.astype(int)  ---->	to convert the datatype of newly created column(EXITSn_hourly) from float(default) to int.
5. 	Writing back the returned dataframe (output_dataframe) to "output_file.txt" which will be used in next exercise.
	If we don't write index=None , an extra column will be added to output file showing row index 
	Note ---->	 Now the 'output.txt' of Exercise 1.4 will be overwritten by the 'output.txt' created in point 4 .
'''