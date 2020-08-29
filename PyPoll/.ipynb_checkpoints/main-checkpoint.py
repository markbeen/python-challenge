import os
import csv
import statistics
import time

# Path to collect data from the Resources folder
pathToCSV = '//128.143.15.11/markX/DataBootCamp/HomeWork/03-Python/Instructions/PyPoll/'

election_csv = os.path.join(pathToCSV, 'Resources', 'election_data.csv')

##### Open election csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")    # use reader to create object
    csv_header = next(csv_file)      # Read the header row first (this will also make file go to next row)
    voterID = []         # make empty list so that I can append in loop
    county = []     # make empty list so that I can append in loop
    candidate = []  # make empty list so that I can append in loop

    i = 0 # this was used simply to evaluate a small portion of the file
##### For loop to grab month and profit data
    for iRow in csv_reader:
        voterID.append(iRow[0])
        county.append(iRow[1])
        candidate.append(iRow[2])
        i = i+1
        #if i == 1500: # set temp breakpoint  to exit w/o going through entire file
        #    break

##### Get number of total number of voters, names of candidates
totalVoters = len(voterID)
candidateNames = set(candidate) # get unique candidate names
canList = list(candidateNames)  # convert unique candidates into a list

canList2 = [] # This was necessar b/c the order of candidates in the canList changed each time I ran the script. Why?
canVotes = []

for iCan in canList:
    canList2.append(iCan) # now, canList2 can be used as a stable represenation of candidate order, and corresponding vote number order
    canVotes.append(candidate.count(iCan)) # this collects the number of votes per candidate, in the same order as the candidates in canList2

sortedVotes = sorted(canVotes, reverse = True) # sorts vote %age in descending order (i.e. winner to loser)

percentVotes = []
for iCan in canVotes:
    percentVotes.append(round(100*iCan/sum(canVotes),0)) # convert # of votes into % of votes

sortedVotePercent = sorted(percentVotes, reverse = True) # sorts vote %age in descending order (i.e. winner to loser) (check out https://www.programiz.com/python-programming/methods/list/sort)

winnerToLoser = []
for iCans in sortedVotePercent:
    winnerToLoser.append(canList2[percentVotes.index(iCans)]) # appends candidate to winnerToLoser, in the order of vote %, biggest to smallest

###### Print Results
print("Election Results")
print("-" *30)
print(f"Total Votes: {totalVoters}")
print("-" *30)

for index, elem in enumerate(winnerToLoser):
    print(f"{winnerToLoser[index]}: {'{0:.3f}'.format(sortedVotePercent[index])}% ({sortedVotes[index]})")

print("-" *30)
print(f"Winner: {winnerToLoser[0]}")
print("-" *30)


##### Write to file
# Path to directory to save file
pathToTextFile = '//128.143.15.11/markX/DataBootCamp/HomeWork/03-Python/python-challenge/PyPoll/PollResults.txt'
fileOut = open(pathToTextFile,"w") 

fileOut.write("Election Results\n")
fileOut.write("-" *30)
fileOut.write("\n")
fileOut.write(f"Total Votes: {totalVoters}\n")
fileOut.write("-" *30)
fileOut.write("\n")

for index, elem in enumerate(winnerToLoser):
    fileOut.write(f"{winnerToLoser[index]}: {'{0:.3f}'.format(sortedVotePercent[index])}% ({sortedVotes[index]})\n")

fileOut.write("-" *30)
fileOut.write("\n")
fileOut.write(f"Winner: {winnerToLoser[0]}\n")
fileOut.write("-" *30)