# Poll Data Analyzed with Vanilla Python

Objective: To count votes cast in favor of various candidates from a dataset too large for Excel.

A note about the dataset: Votes were codified as a string of the candidate name. Voter ID (presumably a unique key) and county information were also supplied.

Enjoyable Success: Produced a truly sublime and minimal for loop with a dictionary that either added a key and value, or summed the value for that key.


### With Jupyter Notebook & Pandas:

Objective: To count votes cast in favor of various candidates from a dataset too large for Excel.

A note about the dataset: Votes were codified as a string of the candidate name. Voter ID (presumably a unique key) and county information were also supplied.

Enjoyable Success: df['candidate'].Value_Counts() was an especially convenient command, given the structure of the data. Value_Counts(1) produced the votes as a proportion of the total.
