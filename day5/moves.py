import re

with open('day5\sample.txt') as data:
    stacks, moves = data.read().split('\n\n')
    moves = re.findall(r'\d',moves)

counter = 0

while counter != len(moves):
    cratesToMove, fromStack, toStack = moves[counter],moves[counter+1],moves[counter+2]
    counter += 3
    print(cratesToMove,fromStack,toStack)

