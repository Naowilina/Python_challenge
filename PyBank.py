import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
# To store the file path associated with the file and export the result in to analysis.txt file
file = "analysis/financial_analysis.txt"
f = open("analysis/financial_analysis.txt","w")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Convert the dataset into a list
    csvrow = list(csvreader)
    
    
    # Count the total number of months
    months = len(csvrow)
    

    # Calculate the net total amount of "Profit/Losses" over the entire period
    total = 0
    for i in range(len(csvrow)):
        total = total + int(csvrow[i][1])


    # Calculate the average of the changes in "Profit/Losses" over the time period
    begin_year = int(csvrow[0][1])
    end_year = int(csvrow[len(csvrow)-1][1])
    total_change = end_year - begin_year
    average_change = total_change / (int(len(csvrow))-1)


    # Find the greatest increase in profits and decrease in losses (date and amount) over the entire period
    greatest_increase = 0
    greatest_decrease = 0
    for i in range(len(csvrow)-2):
        change = int(csvrow[i+1][1]) - int(csvrow[i][1])
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = csvrow[i+1][0]
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = csvrow[i+1][0]
    

    # Print out the summary in Terminal and import the result into text.file
    print(f"""Financial Analysis
------------------------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})""")
    print(f"""Financial Analysis
------------------------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})""", file = f)


f.close()