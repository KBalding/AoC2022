with open('input.txt','r') as data:
    lines = data.readlines()
    lines.append('\n')
   # data = [line.strip() for line in data]

s,max=0,0
maxList =[]
# find the highest value seperated by blank line
for line in lines:
    if(line != '\n'):
        s = s +int(line)
    else:
        if (max < s):
            max=s
            maxList.append(s)
        s = 0
        #print(max)
maxList.sort()
print('answer=',maxList[-1])

print( maxList[-3:])
print( sum(maxList[-3:]))

