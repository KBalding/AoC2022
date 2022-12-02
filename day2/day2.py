with open('day2\input.txt') as data:
    data = data.readlines()
    data = [line.strip().replace(" ","") for line in data]


outcomes = {
    "AX":4, "AY":8, "AZ":3, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":7, "CY":2, "CZ":6 
}
score = 0

for i in data:
    score += outcomes[i]

print(score)



# p2
p2outcomes = {
    "AX":3, "AY":4, "AZ":8, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":2, "CY":6, "CZ":7 
}

p2score = 0
for i in data:
    p2score += p2outcomes[i]

print(p2score)