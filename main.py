#Import necessary modules
import os
import csv

def export_to_text_file(filename, content):
    output_path = os.path.join(os.getcwd(), filename)
    with open(output_path, 'w') as file:
        file.write(content)
    print(f"Results have been exported to '{filename}'.")

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

#Make the results into a text string
financial_analysis_output = """
                                  Financial Analysis
---------------------------------------------------------------------------------------------------
Total Months: {}

Total: {}

Average Change: {}

Greatest Profit Increase: {} {}

Greatest Profit Decrease: {} {}
""".format(Total_Months, Total_Cash, Change_Average, Max_Change_Month, Max_Change, Min_Change_Month, Min_Change)

#export this string that was just created
export_to_text_file('part1.txt', financial_analysis_output)

#Part 2 -------------------------------------------------------------------------------------------------------------------

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


#Make results into a string and export results to a Text File

election_results_output = """
Election Results
-----------------------------
Total Votes: {}

-----------------------------
{}
-----------------------------
The winner is {}

-----------------------------
""".format(Total_Votes, "\n".join("{}: Received {} total votes, ({:.2f}%)".format(person, Candidate.count(person), (Candidate.count(person) / Total_Votes) * 100) for person in Unique_Candidate), Winner)

# Export the election results to a text file
export_to_text_file('part2.txt', election_results_output)

#Make each text file into 1
merged_output = ""

# Read Part 1
with open('part1.txt', 'r') as file:
    merged_output += file.read()

# Read Part 2
with open('part2.txt', 'r') as file:
    merged_output += file.read()

# Export the merged output to a new text file
export_to_text_file('Main.txt', merged_output)
