

import os
import csv


csvpath = os.path.join('.','Resources','budget_data.csv')
#print(csvpath)

with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     #print(csvreader)
     
     csv_header = next(csvreader)
     #print(f'CSV Header: {csv_header}')
     
# use list comprehension to read in the file
     data = {row[0]:int(row[1]) for row in csvreader}
     
   
count = len(data.keys())
total = sum(data.values())
maxprofit = max(data.values())
minprofit = min(data.values())
average = round(total / count,2)

for k,v in data.items():
    if v == maxprofit:
        maxmonth=k

for k,v in data.items():
    if v == minprofit:
        minmonth=k

        
report = (f"Financial Analysis\n"\
"----------------------------\n"\
f"Total Months: {count}\n"\
f"Total: ${total}\n"\
f"Average Change: ${average}\n"\
f"Greatest Increase in Profits: {maxmonth} (${maxprofit})\n"\
f"Greatest Decrease in Profits: {minmonth} (${minprofit})\n")

print(report)

with open('financial_analysis.txt', 'w') as f:
    f.write(report) 