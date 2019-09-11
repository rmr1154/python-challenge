

import os
import csv

count = 0
total = 0
maxprofit = 0
minprofit = 0
average = 0
lastval = 0
diff = 0
difftotal = 0
diffcount = 0

csvpath = os.path.join('.','Resources','budget_data.csv')
#print(csvpath)

with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     #print(csvreader)
     
     csv_header = next(csvreader)
     #print(f'CSV Header: {csv_header}')
     
     for row in csvreader:
        rowval = int(row[1]) 
        total += rowval
        if count != 0:
            diff = rowval - lastval
            diffcount += 1
        if diff > maxprofit:
            maxprofit = diff
            maxmonth = row[0]
        if diff < minprofit:
            minprofit = diff
            minmonth = row[0]
        lastval = rowval
        difftotal += diff
        count += 1
        #print(f'rowval:{rowval} count:{count} total:{total} diff:{diff} maxprofit:{maxprofit} minprofit:{minprofit} lastval:{lastval} ')

average =  round(difftotal / diffcount,2)
        
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