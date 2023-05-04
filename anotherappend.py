scores = []
for i in  range(3):
   score= int(input("value:"))
scores += [score]

average = sum(scores)/len(scores)
print(f"AVERAGE:{average}")