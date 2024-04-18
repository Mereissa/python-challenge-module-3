import os
import csv

# file Path to collect data
file_path = 'resources\election_data.csv'

# hold the number of votes for each candidate
candidate_votes = {}

#variable to hold the total number of votes
total_votes = 0

#output file
output_dir = os.path.join('analysis')
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

#save the text file
output_file = os.path.join(output_dir, 'election_results.txt')

# keep the file open
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    # Read the header row
    header = next(csvreader)
    # search through each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

#the winner 
winner = max(candidate_votes, key=candidate_votes.get)

#print the results
with open(output_file, 'w') as txt_file:
    # Function to write and print lines
    def write_print(line):
        print(line)
        txt_file.write(line + "\n")
    
    write_print("Election Results")
    write_print("-------------------------")
    write_print(f"Total Votes: {total_votes}")
    write_print("-------------------------")
    
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        write_print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    write_print("-------------------------")
    write_print(f"Winner: {winner}")
    write_print("-------------------------")

# print the output to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
