# Election Analysis

## Overview of Election Audit

A complete and thorough review, audit and analysis was needed for the recently held election in order to determine the winning candidate. The total vote was tallied by both County and Candidate to determine who had the highest count as well as percentage.

## Election Audit Results

With 272,892 votes of a Total Vote count of 369,711, Diana Degette won the election with 73.8% of the votes. The majority of the votes in the election came from Denver with 82.8% and 306,055 votes.

Election Results
-------------------------
Total Votes: 369,711
-------------------------
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Largest County Turnout Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------

## Election Audit Summary

This script can be ran on any election with small modifications to the code. Simply referencing a .csv file with the same formatting, can result in the same type of analysis. 

There are other variations that could be used to view other sets of data such as demographics, etc. You could alter the code below to reference other items in lieu of the Largest County. 


candidate_options = []
candidate_votes = {}

county_names = []
county_votes = {}
                    
winning_candidate = ""
winning_count = 0
winning_percentage = 0

largest_county_turnout = ""
largest_county_vote = 0
