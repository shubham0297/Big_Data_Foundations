'''
Exercise 3.2				REDUCER CODE ( ENTRIESn_hourly per UNIT )

Problem Statement :

Now, create the reducer. Given the mapper result from the previous exercise, the reducer must print (not return) one line per UNIT, with the total number of ENTRIESn_hourly during May (which is our data duration), separated by a tab. An example of exit line from the reducer may look like this: 'R001 \ t500625.0'

You can assume that the entry for the reducer is ordered in a way that all lines corresponding to a particular unit are grouped. However, the reducer exit will have repetition, as there are stores that appear in different files' locations.

Export your reducer into a file named reducer_result.txt and send it with your submission.
'''

#Solution :

import sys

sys.stdin = open('mapper_result.txt','r').readlines()       # Point 1 
sys.stdout = open('reducer_result.txt', 'w')                # Point 2

def reducer():
    
    total=0                  
    oldKey=None
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped)!=2:                             # Point 3
            continue;
        key, value = data_mapped                            # Point 4
        if oldKey and oldKey != key:                        # Point 5 
            print (oldKey, "\t", total)
            oldKey = key;
            total = 0                                       # Point 6 

        oldKey = key
        total += float(value)                               # Point 7 

    if oldKey != None:                                      # Point 8  
        print (oldKey, "\t", total)


        
reducer()




'''
KEY POINTS

1.  Reads the 'mapper_result.txt' file. 
    NOTE ---> 'mapper_result.txt' MUST BE PRESENT IN THE SAME FOLDER IN WHICH THIS CODE(Reducer.py) IS.
2.  Creates(Overwrites if already present) a file named 'reducer_result.txt' and writes the whatever is printed in sys.stdout in it.
3.  If result from mapper has more or less than 2 columns then ..skip it.
4.  Else set UNITS=key and ENTRIESn_hourly as value. ( If result from mapper has exactly 2 columns).
5.  Printing the UNIT and total ENTRIESn_hourly once per UNIT as soon as oldKey!=key. (When new key is found, we print the result of oldKey)
6.  Set total =0 for next UNIT (When new key is found)
7.  Keep adding total to previous total ..while oldKey and key are same.
8.  For printing the last UNIT.
'''
