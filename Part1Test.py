#Import necessary modules
import os
import csv



#Pull in CSV files and path it
csvpath = os.path.join('..', 'python-challenge-isaac-gish', 'Resources', 'budget_data.csv')

#Save lists
Months = []
Cash = []


#Open CSV file and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#Read headers when reading
    csvheader = next(csvreader)

    for row in (csvreader):
        #Apply column 0 to months
        Months.append(row[0])
        #Apply column 1 to cash and convert cash to digits
        Cash.append(float(row[1]))

#New Variables - Number of months and sum of profits and losses
Total_Months = len(Months)
Total_Cash = sum(Cash)

#Create Title
print("                                  Financial Analysis")
#Make it easier to read
print("---------------------------------------------------------------------------------------------------")
#Print out the number of months
#1.
print(f"Total Months: {Total_Months}")
print("")
#Print out the sum of the profits and losses
#2.
print(f"Total: {Total_Cash}")
print("")
#Define Variables to find the average change
#Find each change
Changes = [Cash[i+1] - Cash[i] for i in range(len(Cash)-1)]
#Add each change 
Total_Changes = sum(Changes)
#Find the average of each change
Change_Average = (Total_Changes/len(Changes))

#Print the average change
#3.
print(f"Average Change:  {Change_Average}")
print("")
#Define variables to find the max and minimum changes in profit
Max_Change = max(Changes)
#Find the index for changes
Max_Change_Index = Changes.index(Max_Change)
#Find the month associated with the index of max change, adding 1 because the value of the changes is only 85. 
Max_Change_Month = Months[Max_Change_Index + 1]

Min_Change = min(Changes)
#Repeat above steps but for the min index and month assoicated with this
Min_Change_Index = Changes.index(Min_Change)
Min_Change_Month = Months[Min_Change_Index + 1]
#4.
print(f"Greatest Profit Increase: {Max_Change_Month} {Max_Change}")
print("")
#5.
print(f"Greatest Profit Decrease: {Min_Change_Month} {Min_Change}")
print("")










