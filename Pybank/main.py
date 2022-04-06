
import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "financial_analysis.txt")
with open(csvpath, encoding='utf-8') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    total_months =0
    total = 0
    cur_val=[]
    prev_val= []
   
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
       
        diff_list.append(Diff)
        diff1 = diff1+ Diff
        if total_months < 2: 
            Avg_change =0
        else: 
            Avg_change = round(diff1/(len(diff_list)-1), 2)
            total += int((row[1]))
        prev_row = row
        diff2 = Diff
    max_val = max(diff_list)
    max_val_month = months[diff_list.index(max_val)]
    min_val = min(diff_list)
    min_val_month = months[diff_list.index(min_val)]
       
    with open(output_file, "w") as txt_file:
     financial_analysis = (f"""
     Financial Analysis
     -------------------------
        Total Months: {total_months}
        Total: ${total}
        Average Change: {Avg_change}
        Greatest Increase in Profits: {max_val_month} {max_val}
        Greatest Decrease in Profits: {min_val_month} {min_val}
     -------------------------         
                             """)
    print(financial_analysis)
    
    with open(output_file, "w") as txt_file:
        for lines in financial_analysis:
            txt_file.write(lines)

   
     