import os
import csv

# Path to collect data from the Resources folder
file_path = 'Analysis\Resources\Budget_data.csv'

#Variables for total months, profit losses and previous values
total_months = 0
total_profit_losses = 0
previous_value = None
changes = []

# varibals for greates increase and decrease
greatest_increase = ["",0]
greatest_decrease = ["",float("inf")]

# Open file for data
with open(file_path) as csvfile:

    #spit data with commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # read the header row first
    header = next(csvreader)
    
    first_row =next(csvreader)
    previous_value = int(first_row[1])
    total_profit_losses += previous_value
    total_months += 1
    
    # read all rows after header
    for row in csvreader:
    
        #count the total number of months
        total_months += 1

        #total amount of profit and losses
        total_profit_losses += int(row[1])
        if previous_value is not None:
            change = int(row[1])- previous_value
            changes.append(change)

            # search for gratest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase[0] = row [0]
                greatest_increase[1] = change

                if change < greatest_decrease[1]:
                    greatest_decrease[0] = row[0]
                    greatest_decrease[1] = change

            previous_value = int(row[1])

    #what is the average change
    if len(changes) > 0:
        average_change = sum(changes) / len(changes)
    else: 
        average_change = 0

    # print out the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
