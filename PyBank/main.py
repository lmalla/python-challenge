import os
import csv

#path
path_csv = os.path.join("Resources","budget_data.csv")

Total_Months = 0
Total_Amount = 0
Initial_Profit = 0
Monthly_Changes = []
Total_Change_Profit = 0
Date = []

#open and read csv

with open(path_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read Header
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    #Reading first row
    first_row = next(csv_reader)
    Total_Months += 1
    Total_Amount += int(first_row[1])
    Initial_Profit = int(first_row[1])

    #Read each row after header
    for row in csv_reader:
        Total_Months = Total_Months + 1
        Date.append(row[0])
        Total_Amount = Total_Amount + int(row[1])
        Final_Profit = int(row[1])
        Profit_Losses = Final_Profit - Initial_Profit
        Monthly_Changes.append(Profit_Losses)
        Total_Change_Profit = Total_Change_Profit + Profit_Losses
        Initial_Profit = Final_Profit
        
    Greatest_Increase  = max(Monthly_Changes)
    Greatest_Increase_Date = Date[Monthly_Changes.index(Greatest_Increase)]
    Greatest_Decrease  = min(Monthly_Changes)
    Greatest_Decrease_Date = Date[Monthly_Changes.index(Greatest_Decrease)]
    a = sum(Monthly_Changes)
    b = len(Monthly_Changes)
    Average = a/b

    print(f" Financial Analysis")
    print(f" -------------------------")
    print(f" Total Months: {Total_Months}")
    print(f" Total: ${Total_Amount}")
    print(f" Average Change: ${(round(Average,2))}")
    print(f" Greatest Increase in Profits: {Greatest_Increase_Date } (${Greatest_Increase})")
    print(f" Greatest Decrease in Profits: {Greatest_Decrease_Date } (${Greatest_Decrease})")

output_path = os.path.join("analysis", "PyBank_Result.txt")
with open(output_path,"w") as txtfile:
    csvwriter = csv.writer(txtfile)
    txtfile.write(f" Financial Analysis \n")
    txtfile.write(f" -------------------------\n")
    txtfile.write(f" Total Months: {Total_Months} \n")
    txtfile.write(f" Total: ${Total_Amount} \n")
    txtfile.write(f" Average Change: ${(round(Average,2))} \n")
    txtfile.write(f" Greatest Increase in Profits: {Greatest_Increase_Date } (${Greatest_Increase}) \n")
    txtfile.write(f" Greatest Decrease in Profits: {Greatest_Decrease_Date } (${Greatest_Decrease})")









    
        



