
'''
Exercise 1.4				CREATING NEW COLUMN IN DATAFRAME(ENTRIESn_hourly)

Problem Statement :

The NYC Subway data has cumulative entry and exit data in each line. Let's assume you have a Dataframe called df, which contains only lines for one particular turnstile (unique SCP, C/A, and UNIT). The following function must change these cumulative entries for counting all entries since the last reading (entries from the last line of the Dataframe).

More specifically, there are two things you should do:

1 - Create a new column, called ENTRIESn_hourly 2 - Insert in this column the difference between ENTRIESn in the current and the previous column. If the line has any NAN, fill it out/replace by 1.

Tip: The funtions shift() and fillna() in Pandas might be usefull for this exercise.

Below you will find and example of how your Dataframe should look by the end of this exercise:

    C/A  UNIT       SCP     DATEn     TIMEn    DESCn  ENTRIESn    EXITSn  ENTRIESn_hourly
0     A002  R051  02-00-00  05-01-11  00:00:00  REGULAR   3144312   1088151                1
1     A002  R051  02-00-00  05-01-11  04:00:00  REGULAR   3144335   1088159               23
2     A002  R051  02-00-00  05-01-11  08:00:00  REGULAR   3144353   1088177               18
3     A002  R051  02-00-00  05-01-11  12:00:00  REGULAR   3144424   1088231               71
4     A002  R051  02-00-00  05-01-11  16:00:00  REGULAR   3144594   1088275              170
5     A002  R051  02-00-00  05-01-11  20:00:00  REGULAR   3144808   1088317              214
6     A002  R051  02-00-00  05-02-11  00:00:00  REGULAR   3144895   1088328               87
7     A002  R051  02-00-00  05-02-11  04:00:00  REGULAR   3144905   1088331               10
8     A002  R051  02-00-00  05-02-11  08:00:00  REGULAR   3144941   1088420               36
9     A002  R051  02-00-00  05-02-11  12:00:00  REGULAR   3145094   1088753              153
10    A002  R051  02-00-00  05-02-11  16:00:00  REGULAR   3145337   1088823              243
'''




#Solution :

import pandas

input_dataframe = pandas.read_csv("output_file.txt");					# Point 1

def get_hourly_entries(df):
    
    df['ENTRIESn_hourly']=df['ENTRIESn']-df['ENTRIESn'].shift(1)  		# Point 2
    df.fillna(value=1,inplace=True)                     				# Point 3 
    df.ENTRIESn_hourly = df.ENTRIESn_hourly.astype(int)  				# Point 4
    
    return df

output_dataframe = get_hourly_entries(input_dataframe)					
output_dataframe.to_csv("output_file.txt",index=None)					# Point 5




'''
KEY POINTS

1.	NOTE ---->	'output.txt' is the output file of Exercise 1.3 . IT MUST BE PRESENT IN THE SAME FOLDER IN WHICH  this code( New_Column(ENTRIESn_hourly).py	) is.
2.	This line adds a new column ENTRIESn_hourly and assigns to it the value of difference of ENTRIESn column of ith and i-1 row. 		
	dataframe.shift(x) shifts the dataframe by x units.
3.	dataframe.fillna(value=x)  ----> fills the NAN values with x.
4.	dataframe.astype(int)  ---->	to convert the datatype of newly created column(ENTRIESn_hourly) from float(default) to int.
5. 	Writing back the returned dataframe (output_dataframe) to "output_file.txt" which will be used in next exercise.
	If we don't write index=None , an extra column will be added to output file showing row index 
	Note ---->	 Now the 'output.txt' of Exercise 1.3 will be overwritten by the 'output.txt' created in point 4 .
'''