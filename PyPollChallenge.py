

import os
import csv
import operator
csvpath = os.path.join('election_data.csv')


competitors = {}
competitors2 = {}


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        competitors[row[2]] = competitors.get(str(row[2]), 0) + 1


total_count = sum(competitors.values(), 0.0)
competitors2 = {k: v / total_count for k, v in competitors.items()}


# I wanted to add an index to the dict to auto-grow my print function, but I ran out of time.

# def get_nth_key(competitors2, n=0):
#     if n < 0:
#         n += len(competitors2)
#     for i, key in enumerate(competitors2.keys()):
#         if i == n:
#             return key
#     raise IndexError("dictionary index out of range") 



winner = max(competitors.items(), key=operator.itemgetter(1))[0]
winner_print = 'Winner: ' + str(winner)
total_votes_print = 'Total Votes: ' + str(total_count)


khan_votes = 'Khan: ' + str((round(competitors2['Khan'], 3))) + '% (' + str(competitors['Khan']) + ')'
correy_votes = 'Correy: ' + str((round(competitors2['Correy'], 3))) + '% (' + str(competitors['Correy']) + ')'
li_votes = 'Li: ' + str((round(competitors2['Li'], 3))) + '% (' + str(competitors['Li']) + ')'
oTooley_votes = "O'Tooley: " + str((round(competitors2["O'Tooley"], 3))) + '% (' + str(competitors["O'Tooley"]) + ')'



cache = []
cache.append("Election Results")
cache.append("-------------------------")
cache.append("Total Votes: 3521001")
cache.append("-------------------------")
cache.append(khan_votes)
cache.append(correy_votes)
cache.append(li_votes)
cache.append(oTooley_votes)
cache.append("-------------------------")
cache.append("Winner: " + str(winner))
cache.append("-------------------------")

print(cache)

with open('output2.txt', 'w') as output:
  for line in cache:
      output.write("%s\n" % line)