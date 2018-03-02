'''
Exercise 1.2             COMPILING THE DOWNLOADED FILES

Problem Statement :		

Write down a function that takes the list of all names of the files you downloaded in Exercise 1.1 and compile them into one single file. There must be only one header line in the output file.

For example, if file_1 has: line 1... line 2...

and the other file, file_2, has: line 3... line 4... line 5...

We must combine file_1 and file_2 into one master file, as follows:

'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn' line 1... line 2... line 3... line 4... line 5...
'''





#Solution :

filenames = {"turnstile_030617.txt","turnstile_100617.txt","turnstile_170617.txt","turnstile_240617.txt"}		#	Point 1	

def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,STATION, LINENAME, DIVISION, DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in sorted(filenames):  				 # 	Point 2
            with open(filename,'r') as currentFile:   		 # 	Point 3
                next(currentFile)							 # 	Point 4
                master_file.write(currentFile.read())    	 #	Point 5
    return None



create_master_turnstile_file(filenames,'output_file.txt'); 	 # 	Point 6	




'''
KEY POINTS

1.  filenames contains list of all the files. 
	NOTE ---->	ALL THE DOWLOADED FILES FROM EXERCISE 1.1 MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS Compiling_Files.py FILE IS
2.	Sorted is used to display the files in sequential order(like content of file1 will be appended first then file2 and so on) ..otherwise it appends randomly(no ordering).
3.	Opens the current file from the list of filenames
4.	next(filename) ----> Skips the first line of the file (common header line)
5.	Writes the complete content of currently opened file into master file as a single string.
	file.read() ----> Extracts a string that contains all characters in the file(reads the whole file as a string). 
6.	We pass (filename , 'output_file.txt') --> Here output_file.txt is the name which we want to give to the file which will contain the Compbined data of all the files.   
'''
	