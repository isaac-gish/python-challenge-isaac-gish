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

#New Variables
Total_Months = len(Months)
Total_Cash = sum(Cash)
#Create Title
print("                                  Financial Analysis")
#Make it easier to read
print("---------------------------------------------------------------------------------------------------")

print(f"Total Months: {Total_Months}")

print(f"Total:  {Total_Cash}")

#Define Variables 






