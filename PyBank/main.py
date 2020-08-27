import os
import csv
import statistics
import time

# Path to collect data from the Resources folder
pathToCSV = '//128.143.15.11/markX/DataBootCamp/HomeWork/03-Python/Instructions/PyBank/'

budget_csv = os.path.join(pathToCSV, 'Resources', 'budget_data.csv')

##### Open budget csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")    # use reader to create object
    csv_header = next(csv_file)      # Read the header row first (this will also make file go to next row)
    months = []         # make empty list so that I can append in loop
    profitLoss = []     # make empty list so that I can append in loop
    monthlyChange = []  # make empty list so that I can append in loop


##### For loop to grab month and profit data
    for iRow in csv_reader:
        months.append(iRow[0])
        profitLoss.append(int(iRow[1]))

##### Get number of months, sum of profits and mean of profits (needed to import statistics)
numMonths = len(months)
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
pathToTextFile = '//128.143.15.11/markX/DataBootCamp/HomeWork/03-Python/python-challenge/PyBank/FinancialAnalysis.txt'
fileOut = open(pathToTextFile,"w") 

fileOut.write("Financial Analysis\n")
fileOut.write("-" *30)
fileOut.write("\n")
fileOut.write(f"Total Months: {numMonths}\n")
fileOut.write(f"Total Profit: ${netProfitLoss}\n")
fileOut.write(f"Average Change: ${meanProfitChange}\n")
fileOut.write(f"Greatest Increase in Profits: {monthMaxProfit} (${maxProfit})\n")
fileOut.write(f"Greatest Decrease in Profits: {monthMinProfit} (${minProfit})\n")