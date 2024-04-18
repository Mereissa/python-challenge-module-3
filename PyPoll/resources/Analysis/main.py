import os
import csv

# Path to collect data from the Resources folder
file_path = 'resources\election_data.csv'

# Replace this string with your actual CSV content
data_string = """
Ballot ID,County,Candidate
1323913,Jefferson,Charles Casper Stockham
... (other rows omitted for brevity) ...
1640901,Jefferson,Charles Casper Stockham
"""

# Convert the string to a file-like object
data = StringIO(data_string)

# Read the data into memory
reader = csv.DictReader(data)

# Initialize vote count dictionary
candidate_votes = defaultdict(int)

# Count votes
for row in reader:
    candidate_votes[row['Candidate']] += 1

# Total number of votes
total_votes = sum(candidate_votes.values())

# Calculate percentage and determine winner
max_votes = 0
winner = ''
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Prepare the results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print the results to the terminal
for line in results:
    print(line)

# Save the results to a text file
with open('election_results.txt', 'w') as file:
    for line in results:
        file.write(f"{line}\n")

