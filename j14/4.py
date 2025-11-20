from random import *

people = ["sara", "ali", "sana", "reza", "ana", "mohammad"]
winners = []
# a = int(input("enter num of winners: "))
a = 4

for i in range(a):
        winner = choice(people)
        winners.append(winner)
        people.remove(winner)

for i in range(len(winners)):
    print(i+1, "->", winners[i])
