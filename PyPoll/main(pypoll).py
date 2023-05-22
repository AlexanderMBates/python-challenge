# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\15126\Downloads\UTA-VIRT-DATA-PT-04-2023-U-LOLC-main\UTA-VIRT-DATA-PT-04-2023-U-LOLC-main\02-Homework\03-Python\Starter_Code\PyPoll\Resources\election_data.csv"

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #setting up variables
    total_votes = 0
    candidates = []
    id = []
    vote_w = []
    charles = 0
    charlesp = 0.0
    diana = 0
    dianap = 0.0
    raymon = 0
    raymonp = 0.0
    winner = ""

    
    # Read each row of data after the header
    for row in csvreader:
        
        #counts total votes
        total_votes = total_votes + 1
        
        #obtains unique candidates for the whole set
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == "Charles Casper Stockham" :
            charles = charles + 1
        
        if row[2] == "Diana DeGette" :
            diana = diana + 1

        if row[2] == "Raymon Anthony Doane" :
            raymon = raymon + 1

    #finding candidate percentages
    charlesp = round((charles/total_votes)*100,3)
    dianap = round((diana/total_votes)*100,3)
    raymonp = round((raymon/total_votes)*100,3)

    #determines winner based on vote count
    if diana > charles and diana > raymon:
        winner = candidates[1]
    elif charles > diana and charles > raymon:
        winner = candidates[0]
    else:
        winner = candidates[2]
      
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print("Charles Casper Stockham: " + str(charlesp) + "% (" + str(charles) + ")" )
    print("Diana DeGette: " + str(dianap) + "% (" + str(diana) + ")" )
    print("Raymon Anthony Doane: " + str(raymonp) + "% (" + str(raymon) + ")" )
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

    #writing to the a seperate text file
    f = open("analysis.txt", "w")
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write("Total Votes: " + str(total_votes) + "\n")
    f.write("-------------------------\n")
    f.write("Charles Casper Stockham: " + str(charlesp) + "% (" + str(charles) + ")\n" )
    f.write("Diana DeGette: " + str(dianap) + "% (" + str(diana) + ")\n" )
    f.write("Raymon Anthony Doane: " + str(raymonp) + "% (" + str(raymon) + ")\n" )
    f.write("-------------------------\n")
    f.write("Winner: " + winner + "\n")
    f.write("-------------------------\n")
    f.close()