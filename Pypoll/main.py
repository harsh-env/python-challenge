
import os
import csv
#for this code to work, we need to sort the csv file by Column C
csvpath = os.path.join("Resources", "election_data_check.csv")
output_file = os.path.join("analysis", "election_analysis.txt")

Total_Votes=0
can_names = []
can_votes = {} 
selected_votes=[]
selected_vote_percent=[]
# dict()
Winning_Candidate = ""
Winning_Count =0
can_nm1 = ""
# can_num
with open(csvpath, encoding='utf-8') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        Total_Votes += 1
        can_n = row[2]
        if can_n != can_nm1:
        # if can_n != can_nm1:
            can_names.append(can_n)
            # can_number +=1
            can_votes[can_n] = 0
            can_votes[can_n] += 1
        else:
            can_votes[can_n] += 1
            
        can_nm1 = can_n
        
        for candidate in can_votes:
            votes = can_votes.get(candidate)
            vote_percent = round((float(votes)/float(Total_Votes))*100, 3)
            
            # can_votes[candidate] = votes
            # if votes > Winning_Count: 
            #     Winning_Count = votes
            #     Winning_Candidate = can_n
    # print(can_votes, vote_percent, "%")
    # print(can_votes)
    # , vote_percent, "%")
# print(can_votes.keys, can_names[1])
# print(can_votes.items())
# print(can_names[1], selected_votes[1], selected_vote_percent[1])

print(Total_Votes)
# print({votes})

# print(votes)
# print(vote_percent)
# print(Winning_Candidate)

# with open(output_file, "w") as txt_file:
#      election_results = (f"""
#     Election Results
#     -------------------------
#     Total Votes: {Total_Votes}
#     -------------------------  
#     {can_n}: {vote_percent} {votes}
#     {can_n}: {vote_percent} {votes}
#     {can_n}: {vote_percent} {votes}
#     ------------------------- 
#     # Winner : {Winning_Candidate}          
#                     """)
# print(election_results)


    
    # Tot_Count = 0




    # Old_Value = ""
    # Counter = 1
    # count_list= []
    # for row in csvreader:
    #     Tot_Count +=1
    #     cur_val = (row[2])
    #     # Counter = Counter + 1
    #     if cur_val == Old_Value:
    #         Counter = Counter + 1
    #         count_list.append(Counter)
    #         # A = len(count_list)
    #     if Counter == 1: 
    #         print(cur_val)
    #     if cur_val != Old_Value:
    #             Stop_Val = Old_Value
    #             print(Stop_Val, len(count_list))
    #             Counter = 1
    #     Old_Value = cur_val
        
              
    # print("Total Number of Votes Cast:", Tot_Count)
    # ##RAN OUT OF TIME - I THINK I CAN FIX THIS CODE
   