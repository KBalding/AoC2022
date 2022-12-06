with open('day6\input.txt') as data:
    data = data.readlines()
    # data = [line.strip() for line in data]
   

# print(data)

char1, char2, char3, char4 = 0, 0, 0, 0
counter = 0


for i in data:
    while counter != len(i)-3:
        char1, char2, char3, char4 = i[counter],i[counter+1],i[counter+2],i[counter+3]
        signal = (char1,char2,char3,char4)
        # char1 = i[counter]
        counter += 1
        # print("normal",signal)
        setSignal = set(signal)
        # print(setSignal)
        if len(setSignal) ==4:
            print(counter+3)
            print(setSignal)
            break





     