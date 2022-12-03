import string

with open('day3\input.txt') as data:
    data = data.readlines()
    data = [line.strip() for line in data]


dict1=dict(zip(string.ascii_lowercase, range(1,27)))
dict2=dict(zip(string.ascii_uppercase, range(27,53)))
dict1.update(dict2)
# dict1 = {'p':10}


# Need to perform the same logic but have the 
comp1 = 0
comp2 = 0
common =()
priority=0
counter = 0

while counter != len(data):
    comp1, comp2, comp3 = data[counter], data[counter+1], data[counter+2]
    # print(comp1,comp2,comp3)
    common = ''.join(set(comp1).intersection(comp2).intersection(comp3))
    counter += 3
    # print(common)
    for x in common:
        priority += dict1[x]
print(priority)