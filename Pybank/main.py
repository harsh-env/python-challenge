# from audioop import avg
# from operator import index
from calendar import month
import os
import csv
import math
# from sqlite3 import Row
# from statistics import mean
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, encoding='utf-8') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header : {csv_header}")
    total_months =0
    total = 0
    cur_val=[]
    prev_val= []
    # next_val=0
    diff1=0
    diff2=0
    Max_Val=0
    diff_list=[]
    Diff=0
    prev_row=0
    months=[]
    for row in csvreader:
        total_months +=1
        months.append(row[0])
        cur_val = int(row[1])
        if total_months<2: 
            prev_val = int(row[1])
        else:
            prev_val = int(prev_row[1])
        Diff = (int(cur_val) - int(prev_val))
        # diff.append(int(cur_val) - int(prev_val))
        # max_val = max(diff)
        diff_list.append(Diff)
          # if int(diff) > int(diff2): 
        #     print(diff, total_months)
        #     Max_Val = diff
        # else:
        #     Max_Val = diff2
        
        diff1 = diff1+ Diff
        if total_months < 2: 
            Avg_change =0
        else: 
            # Avg_change = diff1/(total_months-1)
            Avg_change = diff1/(len(diff_list)-1)
        total += int((row[1]))
        prev_row = row
        diff2 = Diff
    max_val = max(diff_list)
    max_val_month = months[diff_list.index(max_val)]
    min_val = min(diff_list)
    min_val_month = months[diff_list.index(min_val)]
    print("Total Months:", total_months)
    print("Total:", total)
    print("total change:", Avg_change)
    print("Greatest Increase in Profits:", max_val_month, max_val)
    print("Greatest Dncrease in Profits:", min_val_month, min_val)
    # print(diff_list)
    # print(diff[total_months])

    # for i in range
  # else:
            # diff[total_months]= int(row[1])-int(prev_row[1])
        # diff[total_months]= prev_row[1]  