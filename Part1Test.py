#Import necessary modules
import os
import csv

#Pull in CSV files and path it
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Define Variables


#Open CSV file and print
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvfile)
#Read headers when reading
    csvheader = next(csvreader)
    print(f'Budget Header: [{csvheader}]')

    for row in csvreader:
        print(row)

#Print Title
print("Financial Analysis")
#Make it easier to read
print("---------------------------------------------------------------------------------------------------")

