"""
Jon Whisler

Class: CS 521 - Fall

Date: 9/27/2025

Homework Problem # 4_1

Description: Uses data set of comedy video votes, sorts and prints top 10 voted videos.
"""
import operator
voting_records = dict()
# source = open("test.txt")
try:
    source = open("comedy_comparisons.train")
    with open("comedy_comparisons.train") as f:
        for vote in f:
            vote_list = vote.split(",")
            if vote_list[2][0].lower() == "left":
                if vote_list[0] in voting_records:
                    voting_records[vote_list[0]] += 1
                else:
                    voting_records[vote_list[0]] = 1
            else:
                if vote_list[1] in voting_records:
                    voting_records[vote_list[1]] += 1
                else:
                    voting_records[vote_list[1]] = 1
    sorted_voting_records = sorted(
        voting_records.items(), key=operator.itemgetter(1), reverse=True)

    print("The Top 10 Funniest YouTube Videos:")
    for e in range(10):
        print(f"{e + 1:2}. {sorted_voting_records[e][0]}")

except FileNotFoundError:
    print("File not found")
