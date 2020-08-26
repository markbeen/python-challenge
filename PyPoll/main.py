import os
import csv
import statistics
import time

# Path to collect data from the Resources folder
pathToCSV = '//128.143.15.11/markX/DataBootCamp/HomeWork/03-Python/Instructions/PyPoll/'

election_csv = os.path.join(pathToCSV, 'Resources', 'election_data.csv')

##### Open budget csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")    # use reader to create object
    csv_header = next(csv_file)      # Read the header row first (this will also make file go to next row)
    voterID = []         # make empty list so that I can append in loop
    county = []     # make empty list so that I can append in loop
    candidate = []  # make empty list so that I can append in loop

    i = 0
##### For loop to grab month and profit data
    for iRow in csv_reader:
        voterID.append(iRow[0])
        county.append(iRow[1])
        candidate.append(iRow[2])
        i = i+1
        if i == 1500:
            break

##### Get number of months, sum of profits and mean of profits (needed to import statistics)
totalVoters = len(voterID)

candidateNames = set(candidate)

canList = list(candidateNames)

canList2 = []
canVotes = []

for iCan in canList:
    canList2.append(iCan)
    canVotes.append(candidate.count(iCan))

percentVotes = []
for iCan in canVotes:
    percentVotes.append(round(100*iCan/sum(canVotes),2))

[sorted(percentVotes).index(theCans) for theCans in percentVotes]

sortedVotes = sorted(percentVotes)
print(f"sorted votes = {sortedVotes}")

for iCans in sortedVotes:
    theCan = canList2[percentVotes.index(iCans)]
    print(theCan)

#print(percentVotes)

biggestPercentIndex = percentVotes.index(max(percentVotes))
biggestWinner = canList2[biggestPercentIndex]

#print("Election Results")
#print("-" *30)
#print(f"Total Votes: {totalVoters}")
#print("-" *30)


#print(f"Total Profit: ${netProfitLoss}")
#print(f"Average Change: ${meanProfitChange}")
#print(f"Greatest Increase in Profits: {monthMaxProfit} (${maxProfit})")
#print(f"Greatest Decrease in Profits: {monthMinProfit} (${minProfit})")



quit()

netProfitLoss = sum(profitLoss)
meanProfitLoss = statistics.mean(profitLoss)

##### Calculate monthly change in profit (i.e. profit_i+1  -  profit_i)
profitChange = []
for index, elem in enumerate(profitLoss):  # handy emnumerate function (nice way to keep track of index...and therefore the value in the next row)
    if (index+1 < len(profitLoss) and index >= 0):
        currentProfit = profitLoss[index]
        nextProfit = profitLoss[index+1]
        profitChange.append(nextProfit - currentProfit)

##### calculate mean, month-to-month change
meanProfitChange = round(statistics.mean(profitChange),2)

##### Find indices of max and min profit, so that I can get corresponding month
maxProfitIndex = profitChange.index(max(profitChange))
maxProfit = profitChange[maxProfitIndex]
monthMaxProfit = months[maxProfitIndex+1]
minProfitIndex = profitChange.index(min(profitChange))
minProfit = profitChange[minProfitIndex]
monthMinProfit = months[minProfitIndex+1]

##### Print the output
print("Financial Analysis")
print("-" *30)
print(f"Total Months: {numMonths}")
print(f"Total Profit: ${netProfitLoss}")
print(f"Average Change: ${meanProfitChange}")
print(f"Greatest Increase in Profits: {monthMaxProfit} (${maxProfit})")
print(f"Greatest Decrease in Profits: {monthMinProfit} (${minProfit})")


##### Write to file
# Path to directory to save file
pathToTextFile = '//128.143.15.11/markX/DataBootCamp/HomeWork/03-Python/python-challenge/PyBank/test.txt'
fileOut = open(pathToTextFile,"w") 

fileOut.write("Financial Analysis\n")
fileOut.write("-" *30)
fileOut.write("\n")
fileOut.write(f"Total Months: {numMonths}\n")
fileOut.write(f"Total Profit: ${netProfitLoss}\n")
fileOut.write(f"Average Change: ${meanProfitChange}\n")
fileOut.write(f"Greatest Increase in Profits: {monthMaxProfit} (${maxProfit})\n")
fileOut.write(f"Greatest Decrease in Profits: {monthMinProfit} (${minProfit})\n")