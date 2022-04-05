# from audioop import avg
# from operator import index
from itertools import count
from operator import le
import os
import csv
import math
from typing import Counter
# from sqlite3 import Row
# from statistics import mean
csvpath = os.path.join("Resources", "election_data.csv")
# csvpath= "Instructions\\PyPoll\\Resources\\election_data.csv"
with open(csvpath, encoding='utf-8') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header : {csv_header}")
    Tot_Count = 0
    Old_Value = ""
    Counter = 1
    count_list= []
    for row in csvreader:
        Tot_Count +=1
        cur_val = (row[2])
        # Counter = Counter + 1
        if cur_val == Old_Value:
            Counter = Counter + 1
            count_list.append(Counter)
            # A = len(count_list)
        if Counter == 1: 
            print(cur_val)
        if cur_val != Old_Value:
                Stop_Val = Old_Value
                print(Stop_Val, len(count_list))
                Counter = 1
        Old_Value = cur_val
        
              
    print("Total Number of Votes Cast:", Tot_Count)
    ##RAN OUT OF TIME - I THINK I CAN FIX THIS CODE
   