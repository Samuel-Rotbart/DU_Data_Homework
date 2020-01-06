# ## PyBank

import os
import csv

# open and create csvreader
pybank_csv_path = os.path.join("Resources/budget_data.csv")

with open(pybank_csv_path, newline="") as pybankreader:
    pybankreader = csv.reader(pybankreader,delimiter=",")
    header = next(pybankreader)
    
    # set up counter and calculations for p/l differences from row to row
    pl_count = 0
    pl_sum = 0
    cv = 0
    pv = 0
    pl_dif = 0
    pl_dif_list = []
    pl_month_list = []
    pl_list = []
    # loop through all rows and create a list of differences    
    for row in pybankreader:
        pl_count = pl_count + 1
        cv = row[1]
        pl_sum = pl_sum + int(cv)
        pl_dif = int(cv) - int(pv)
        pl_dif_list.append(pl_dif)
        pl_month_list.append(row[0])
        pv = cv
    pl_dif_list[0] = str("x")
    pl_dif_list.remove("x")
    pl_dif_max = max(pl_dif_list)
    pl_dif_min = min(pl_dif_list)
    pl_dif_max_index = pl_dif_list.index(pl_dif_max) + 1
    pl_dif_min_index = pl_dif_list.index(pl_dif_min) + 1
    pl_dif_sum = sum(pl_dif_list)
    pl_dif_avg = round(pl_dif_sum / len(pl_dif_list),2)
    pl_max_month = pl_month_list[pl_dif_max_index]
    pl_min_month = pl_month_list[pl_dif_min_index]
    
    #print output
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(pl_count))
    print("Total: $"+str(pl_sum))
    print("Average Change: $"+str(pl_dif_avg))
    print(f"Greatest Increase in Profits: {pl_max_month} (${pl_dif_max})")
    print(f"Greatest Increase in Profits: {pl_min_month} (${pl_dif_min})")

    #print output to csv
    
    output_path = os.path.join("Resources/new_data.txt")
    with open(output_path,'w') as txtfile:
        
        print("Financial Analysis",file=txtfile)
        print("----------------------------",file=txtfile)
        print("Total Months: "+str(pl_count),file=txtfile)
        print("Total: $"+str(pl_sum),file=txtfile)
        print("Average Change: $"+str(pl_dif_avg),file=txtfile)
        print(f"Greatest Increase in Profits: {pl_max_month} (${pl_dif_max})",file=txtfile)
        print(f"Greatest Increase in Profits: {pl_min_month} (${pl_dif_min})",file=txtfile)
        

