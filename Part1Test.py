#Import necessary modules
import os
import csv

#Pull in CSV files and path it
csvpath = os.path.join('..', 'python-challenge-isaac-gish', 'Resources', 'budget_data.csv')


#Open CSV file and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#Read headers when reading
    csvheader = next(csvreader)





#Define Variables

#Print Title
print("                                  Financial Analysis")
#Make it easier to read
print("---------------------------------------------------------------------------------------------------")

