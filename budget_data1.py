import os
import csv

average_profit = 0
total_change = 0
total_amount = 0
total_months = 0
budget_data = os.path.join("budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    last_change = None
    changes = []

    for row in csv_reader:
        total_months += 1
        
        amount = int(row[1])
        total_amount += amount
        
        if last_change != None:
            change = amount - last_change
            changes.append(change)
                    
        last_change = amount

average_profit = sum(changes) / len(changes)        
   
print(f"Total Months: {total_months}")
print(f"Total Amount: ${total_amount:,}")
print(f"Average Change: ${average_profit: .2f}") 
print(f"Greatest Increase: ${max(changes):,}")
#how add corresponding moth?