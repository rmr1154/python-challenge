

import os
import csv


csvpath = os.path.join('.','Resources','election_data.csv')
#print(csvpath)

with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     #print(csvreader)
     
     csv_header = next(csvreader)
     #print(f'CSV Header: {csv_header}')
     
# use dict comprehension to read in the file
     data = {row[0]:{row[1]:row[2]} for row in csvreader}

# flip the dictionary so that we can count by the lowest level (candidate)
data_flip = {}
for k,v in data.items():
    for k2,v2 in v.items():
        if v2 not in data_flip:
            data_flip[v2] = [1]
        else:
            data_flip[v2].append(1)

# sum up the candidate counts
candidate_cnt = {}
for k,v in data_flip.items():
    candidate_cnt[k] = sum(v)

#build our total count of votes         
votes = len(data.keys())
#find the max votes so we can then lookup key by value
maxvotes = max(candidate_cnt.values())
#lookup key for candidate with the max vote value
for k,v in candidate_cnt.items():
    if v == maxvotes:
        winner=k
        
# build our formatted loop of the candidate totals to inject in the report
nested = ""
for k,v in candidate_cnt.items():
    nested += ("{0}: {1:.3f}% \n".format(k,(v / votes) * 100)) #ya'll trying to trick me with the rounding!!!

# build the report      
report = (f"Election Results\n"\
"----------------------------\n"\
f"Total Votes: {votes}\n"\
"----------------------------\n"\
f"{nested}"\
"----------------------------\n"\
f"Winner: {winner}\n"\
"----------------------------\n")

print(report)

with open('election_results.txt', 'w') as f:
    f.write(report) 