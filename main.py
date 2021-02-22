

def doublelast(j):
   j.append(j[len(j)- 1])
   return j 


print(doublelast(["baby", "shrimp", "moose", "goose"]))