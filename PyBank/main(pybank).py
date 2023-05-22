# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\15126\Downloads\UTA-VIRT-DATA-PT-04-2023-U-LOLC-main\UTA-VIRT-DATA-PT-04-2023-U-LOLC-main\02-Homework\03-Python\Starter_Code\PyBank\Resources\budget_data.csv"

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #variable declarations
    minNum = 0
    minDate = ""
    maxNum = 0
    maxDate = ""
    total = 0
    months = 0
    ave = 0
    daterow = []
    plrow = []
    change = []
    counter = 0

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # total months
        months = months + 1
        
        # total Profit/loss
        total = total + int(row[1])
        
        # putting dates into a list
        daterow.append(row[0])
        
        # putting profit/loss into a list 
        plrow.append(int(row[1]))
        
    #finding changes in between each month
    for line in plrow :
        if counter == len(plrow) - 1 :
            break
        change.append( plrow[counter+1] - plrow[counter])
        
        
        #finding max change
        if change[counter] > maxNum :
            maxNum = change[counter]
            maxDate = daterow[counter+1]
                
        #finding min change
        if change[counter] < minNum :
            minNum = change[counter]
            minDate = daterow[counter+1]
            
        counter = counter + 1
    
    #calculate average of change    
    ave = round(sum(change)/len(change),2)
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(total))
    print("Average Change: $" + str(ave))
    print("Greatest Increase in Profits: " + maxDate + ", " + str(maxNum))
    print("Greatest Decrease in Profits: " + minDate + ", " + str(minNum))
    
    #writing to the a seperate text file
    f = open("analysis.txt", "w")
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(months) + "\n")
    f.write("Total: $" + str(total) + "\n")
    f.write("Average Change: $" + str(ave) + "\n")
    f.write("Greatest Increase in Profits: " + maxDate + ", " + str(maxNum) + "\n")
    f.write("Greatest Decrease in Profits: " + minDate + ", " + str(minNum))
    f.close()

    
