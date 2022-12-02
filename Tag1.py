with open("Tag 1.txt") as file:
    inputList = file.readlines()
#print(inputList)
#Find out how many elves we have
numberOfElves = inputList.count("\n") + 1
print(numberOfElves)


topElf = 0
topCal = 0

#Iterate over all elves and find the maximum
for elf in range(numberOfElves):
    currCal = 0
    for line in range(len(inputList)):
        if (inputList[line] == "\n"):
            break
        else:
            currCal += int(inputList[line][:-1])
    if (currCal > topCal):
        topCal = currCal
        topElf = elf
    currCal = 0
    inputList = inputList[(line+1):]

print(topElf+1)
print(topCal)


print("---------------------------")

with open("Tag 1.txt") as file:
    inputList = file.readlines()
#print(inputList)
#Find out how many elves we have
numberOfElves = inputList.count("\n") + 1
totalCalList = []
#Iterate over all elves and find the maximum
for elf in range(numberOfElves):
    currCal = 0
    for line in range(len(inputList)):
        if (inputList[line] == "\n"):
            totalCalList.append(currCal)
            break
        else:
            currCal += int(inputList[line][:-1])
    currCal = 0
    inputList = inputList[(line+1):]
totalCalList.sort(reverse=True)
print(sum(totalCalList[:3]))
