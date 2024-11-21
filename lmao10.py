n=int(input("Enter total students: "))
print("Enter roll number followed by vote")
votes = {}
rn=[]
vt=[]
for i in range(0,n):
    rn.append(int(input("Enter roll no: ")))
    vt.append(input("A,B or C"))

votes={rn[i]:vt[i] for i in range(0,n)}
voteC={'A':0,'B':0,'C':0}

for roll_no, candidate in votes.items():
    if candidate in voteC:
        voteC[candidate] += 1
print(voteC)

# Display the total votes for each candidate
print(f"Votes for A: {voteC['A']}")
print(f"Votes for B: {voteC['B']}")
print(f"Votes for C: {voteC['C']}")

# Determine the winner (candidate with the maximum votes)
winner = max(voteC, key=voteC.get)

# Declare the winner
print(f"The winner is: {winner}")
