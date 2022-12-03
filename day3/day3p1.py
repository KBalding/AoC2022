import string

with open('day3\input.txt') as data:
    data = data.readlines()
    data = [line.strip() for line in data]


dict1=dict(zip(string.ascii_lowercase, range(1,27)))
dict2=dict(zip(string.ascii_uppercase, range(27,53)))
dict1.update(dict2)
# dict1 = {'p':10}

comp1 = 0
comp2 = 0
common =()
priority=0
for i in data:
    comp1, comp2 = i[:len(i)//2], i[len(i)//2:] 
    for letter in set(comp1):
        if letter in comp2:
            common = tuple(letter)
            # print(common)
            for x in common:
                priority += dict1[x]
                # print(priority)

print(priority)




