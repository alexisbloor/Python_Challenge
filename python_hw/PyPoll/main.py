import os
import csv

electiondata = os.path.join("PyPoll", "Resources", "election_data.csv")
electiondata = r'/Users/alexisbloor/Desktop/Homework/python_hw/PyPoll/Resources/election_data.csv'

votes = []
candidate = []

with open(electiondata) as elect_file:
    csv_reader = csv.reader(elect_file, delimiter=",")
    next(csv_reader)

    for column in csv_reader:
        votes.append(column[0])
        candidate.append(column[2])

    total_votes = len(votes)
    Khan = int(candidate.count("Khan"))
    Correy = int(candidate.count("Correy"))
    Li = int(candidate.count("Li"))
    O_Tooley = int(candidate.count("O'Tooley"))

    K_pct = round((Khan/total_votes), 2)*100
    C_pct = round((Correy/total_votes), 2)*100
    L_pct = round((Li/total_votes), 2)*100
    O_pct = round((O_Tooley/total_votes), 2)*100
    vote_pct = [K_pct, C_pct, L_pct, O_pct]

    print(f"Total Votes: {total_votes}")
    print(vote_pct)
    print(max(vote_pct))

text_file = "/Users/alexisbloor/Desktop/Homework/python_hw/PyPoll/text_file.txt"
with open (text_file, 'w') as text:
    text.write('Election Results')
    text.write('\n----------------')
    text.write(f'\nTotal Votes: {total_votes}')
    text.write('\n----------------')
    text.write(f'\nKhan: {K_pct}% {Khan}')
    text.write(f'\nCorrey: {C_pct}% {Correy}')
    text.write(f'\nLi: {L_pct}% {Li}')
    text.write(f'\nOTooley: {O_pct}% {O_Tooley}')
    text.write(f'\nWinner: Khan')




