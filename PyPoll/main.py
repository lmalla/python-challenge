import os
import csv

#path
path_csv = os.path.join("Resources","election_data.csv")

Total_Number_Of_Votes = 0
List_Of_Candidates = []
No_Of_Votes = []
Vote_Percentage = []

#open and read csv

with open(path_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read Header
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    #Read each row after header
    for row in csv_reader:
        Total_Number_Of_Votes = Total_Number_Of_Votes + 1
        if row[2] not in List_Of_Candidates:
            List_Of_Candidates.append(row[2])
            x = List_Of_Candidates.index(row[2])
            #print(f"It's {x}")
            No_Of_Votes.append(1)
            #print(f"No_Of_Votes is {No_Of_Votes}")
        else:
            x = List_Of_Candidates.index(row[2])
            #print(f"It's {x} again")
            No_Of_Votes[x] += 1
            #print(f"No_Of_Votes is now {No_Of_Votes}")
    
    for Votes in No_Of_Votes:
        Percentage = round(((Votes/Total_Number_Of_Votes) * 100),3)
        Percentage = "%.3f%%" % Percentage
        Vote_Percentage.append(Percentage)
        #print(Vote_Percentage)

Winner = max(No_Of_Votes)
index = No_Of_Votes.index(Winner)
Winning_Candidate = List_Of_Candidates[index]  

print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {Total_Number_Of_Votes}")
print(f"-------------------------------")
for i in range(len(List_Of_Candidates)):
    print(f"{List_Of_Candidates[i]}: {Vote_Percentage[i]} ({No_Of_Votes[i]})")
print(f"-------------------------------")
print(f"Winner: {Winning_Candidate}")
print(f"-------------------------------")

output_path = os.path.join("analysis", "PyPoll_Result.txt")
with open(output_path,"w") as txtfile:
    csvwriter = csv.writer(txtfile)
    txtfile.write(f"Election Results \n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Total Votes: {Total_Number_Of_Votes} \n")
    txtfile.write(f"------------------------------- \n")
    for i in range(len(List_Of_Candidates)):
        txtfile.write(f"{List_Of_Candidates[i]}: {Vote_Percentage[i]} ({No_Of_Votes[i]}) \n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Winner: {Winning_Candidate} \n")
    txtfile.write(f"-------------------------------")

    
    









    
        



