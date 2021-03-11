# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
# 5. The winnder of the election based on popular vote.

# Assign a variable for the file to load and the path. 
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file. 
election_data = open(file_to_load, 'r')
election_data.close()

import csv
dir(csv)
dir(list)

file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
election_data.close()
with open(file_to_load) as election_data:
    print(election_data)

import os
dir(os)
dir(os.path)
os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")

import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Clost the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n_____________________________\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
  