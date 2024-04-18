import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("..", "Resources", "Python-Challenge", "Rescources", "budget_data.csv")
print (csvpath)

# Open file for data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #data = list()

# read the header row first
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")

#read each row of data after the header
for row in csvreader:
    print(row)

# find the number of months
total_months = data['Date'].nunique()

# Sum of Profit and Losses
profit_losses = data['Profit/Losses'].sum()

# difference between profit and losses
changes = data['Profit/Losses'].diff()

#average
average_change = changes.mean()

# Greatest increase in profit
greatest_increase = changes.max()
greatest_increase_data = data.loc[changes.idxmax(), 'Date']

# greatest decrease in profits
greatest_decrease = changes.min()
greatest_decrease_data = data.loc[changes.idxmin(), 'Date']

# Results
analysis_results = {
    'Total Months': total_months,
    'Total Profit/Losses': profit_losses,
    'Average Change': average_change,
    'Greatest Increase in Profits': (greatest_increase_data, greatest_increase),
    'Greatest Decrease in Profits': (greatest_decrease_data, greatest_decrease)
}