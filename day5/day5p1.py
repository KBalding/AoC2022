with open('day5\sample.txt') as data:
    # data = data.readlines()
    # data = [line.strip() for line in data]
    stacks, moves = data.read().split('\n\n')
    crates=stacks[1::4]
    print(crates)
# print(stacks)

hsStacks =[]
hsStacks.append([D])#Dummy to get index1 as stack1 for moves
hsStacks.append(['N','Z'])
hsStacks.append(['D','C','M'])
hsStacks.append(['P'])

# print(hsStacks)

for i in hsStacks:
    # print(i)
    topCrate = i.pop()
    print(topCrate)

# print(moves)

# for instruction in instructions, if target = stack index then pop off no of crates and append to target

