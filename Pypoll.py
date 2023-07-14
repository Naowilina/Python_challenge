import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
# Store the file path associated with the file and export the result in to analysis.txt file
file = "analysis/election_analysis.txt"
f = open("analysis/election_analysis.txt","w")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Convert the csvreader into a list
    csvrow = list(csvreader)
    

    total_votes = len(csvrow)
    print(f"Election Results\n------------------------------------\nTotal Votes: {total_votes}\n------------------------------------")
    print(f"Election Results\n------------------------------------\nTotal Votes: {total_votes}\n------------------------------------", file = f)
    
    
    # Create a list of candidates who received votes
    candidate_list = []
    for i in range(len(csvrow)-1):
        candidate_row = csvrow[i]
        candidate = candidate_row[2]
        # If the candidate is not in the list, add the name into candidate_list
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    
    
    # Creat a dictionary to store the total number of votes each candidate won
    candidate_dict = dict.fromkeys(candidate_list, 0)
    for i in range(len(csvrow)):
        candidate_row = csvrow[i]
        candidate = candidate_row[2]
        candidate_dict[candidate] += 1


    # Calculate the percentage of votes each candidate won
    for i in range(len(candidate_list)):
        candidate = candidate_list[i]
        percentage = "{:.2%}".format(int(candidate_dict[candidate])/total_votes)
        print(f"{candidate_list[i]}: {percentage} ({candidate_dict[candidate]})")
        print(f"{candidate_list[i]}: {percentage} ({candidate_dict[candidate]})", file = f)
    
    
    # Find the winner of the election based on popular vote
    winner = max(candidate_dict, key = candidate_dict.get)
    print(f"------------------------------------\nWinner: {winner}\n------------------------------------")
    print(f"------------------------------------\nWinner: {winner}\n------------------------------------", file = f)


f.close()