with open('day6\input.txt') as data:
    data = data.readlines()
    # data = [line.strip() for line in data]
   

# print(data)

char1, char2, char3, char4 = 0, 0, 0, 0
counter = 0


for i in data:
    while counter != len(i)-13:
        char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14 = i[counter],i[counter+1],i[counter+2],i[counter+3],i[counter+4],i[counter+5],i[counter+6],i[counter+7],i[counter+8],i[counter+9],i[counter+10],i[counter+11],i[counter+12],i[counter+13]
        signal = (char1, char2, char3, char4, char5, char6, char7, char8, char9, char10, char11, char12, char13, char14)
        # char1 = i[counter]
        counter += 1
        print("normal",signal)
        setSignal = set(signal)
        # print(setSignal)
        if len(setSignal) ==14:
            print(counter+13)
            print(setSignal)
            break