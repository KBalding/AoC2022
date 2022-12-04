with open('day4\input.txt') as data:
    data = data.readlines()
    data = [line.strip() for line in data]


elf1, elf2 = 0,0
score=0
elf1min, elf1max, elf2min, elf2max = 0,0,0,0

for i in data:
    elf1, elf2 = i.split(',')
    elf1min, elf1max = elf1.split('-')
    elf2min, elf2max = elf2.split('-')
    elf1min,elf1max,elf2min,elf2max = int(elf1min),int(elf1max),int(elf2min),int(elf2max)
    # print(i)
    if(elf1min <= elf2max) and (elf2min <= elf1max):
        print(elf1,elf2)
        score +=1
print(score)


