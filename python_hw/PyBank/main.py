import os
import csv

bankdata = os.path.join("PyBank", "Resources", "budget_data.csv")
bankdata = r'/Users/alexisbloor/Desktop/Homework/python_hw/PyBank/Resources/budget_data.csv'

# Open and read CSV
with open(bankdata) as bank_file:
    csv_reader = csv.reader(bank_file, delimiter=",")
    next(csv_reader)

    # Get the total months
    total_months = len(list(csv_reader))
    bank_file.seek(0)
    next(csv_reader)

    #Get the net profit
    profit = 0
    change = 0
    lastprofit = 0
    avgprofit = 0
    changes = []
    dates = []
    for row in csv_reader:
        profit += float(row[1])
        change = float(row[1]) - lastprofit
        changes.append(change)
        lastprofit = float(row[1])
        dates.append(row[0])
    changes.remove(changes[0])
    avgprofit = sum(changes)/(len(changes))
    bank_file.seek(0)
    next(csv_reader)
    
    #find the max and min in monthly profit changes
    increase = max(changes)
    decrease = min(changes)
    
    month_increase = changes.index(increase) + 1
    month_decrease = changes.index(decrease) + 1
    
# print results
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months:", total_months)
    print(f"Total: {profit}")
    print(f"Average Change: (${avgprofit})")
    print(f"Greatest Increase in Profits: {dates[month_increase]} (${(str(increase))})")
    print(f"Greatest Decrease in Profits: {dates[month_decrease]} (${(str(decrease))})")

# write to txt file
    text_file = "/Users/alexisbloor/Desktop/Homework/python_hw/PyBank/text_file.txt"
    with open (text_file, 'w') as text: 
        text.write('Financial Analysis')
        text.write('\n----------------')
        text.write(f'\nTotal Months: {total_months}')
        text.write(f'\nTotal: ${avgprofit}')
        text.write(f'\nAvg Change: {changes}')
        text.write(f'\nGreatest Increase in Profits: {dates[month_increase]} (${increase})')
        text.write(f'\nGreatest Decrease in Profits: {dates[month_decrease]} (${decrease})')