#Import necessary modules
import os
import csv



#Pull in CSV files and path it
csvpath = os.path.join('..', 'python-challenge-isaac-gish', 'Resources', 'election_data.csv')

#Save lists
Ballot_ID = []
County = []
Candidate = []

#Open CSV file and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#Read headers when reading
    csvheader = next(csvreader)

#Create a variable to find unique values (for bullet point 2)
    Unique_Candidate = set()

    for row in (csvreader):
        #Apply column 0 to Ballot_ID as a number
        Ballot_ID.append(int(row[0]))
        #Apply column 1 to county
        County.append(row[1])
        #Apply column 2 to candidate 
        Candidate.append(row[2])
        #Make a list containing only the unique names
        Unique_Candidate.add(row[2])
#All print("") are for space and readibility 

#Make the Ballot_ID into a length to count the number of people who voted 
Total_Votes = len(Ballot_ID)
#Print Title
print("")
print("Election Results")
print("")
print("-----------------------------")
print("")
#Print the total amount of columns in the Ballot ID list
print(f"Total Votes: {len(Ballot_ID)}")
print("")
print("-----------------------------")
print("")
#Find the separat candidates, and the votes they received

for person in Unique_Candidate: 
    #Set candidate votes to the votes each candidate received in the iteration of the Candidate list
    Candidate_Votes = Candidate.count(person)
    #Find the percentage of that number
    Vote_Percentage = (Candidate_Votes / Total_Votes) * 100

    print(f"{person}: Received {Candidate_Votes} total votes, ({Vote_Percentage:.2f}%)")
print("")
print("------------------------------")
print("")
#Define Variables for the most votes and winner - set to empty
Max_Votes = 0
Winner = ""
#Set the same loop as before
for person in Unique_Candidate:
    Candidate_Votes = Candidate.count(person)
    #Set the empty variables to store the variable to find only the ones higher than it, and find the matching winner
    if Candidate_Votes > Max_Votes: 
        Max_Votes = Candidate_Votes
        Winner = person
print(f"The winner is {Winner}")
print("")
print("-------------------------------")
