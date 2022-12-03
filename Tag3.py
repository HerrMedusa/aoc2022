def findSimilarChar(rucksack):
    for char in rucksack[0]:
        if char in rucksack[1]:
            return char

def charToPrio(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

with open("Tag 3.txt") as file:
    inputList = [[line[:len(line)//2], line[len(line)//2:].strip()] for line in file.readlines()]    
print(inputList)
prioSum = 0
for rucksack in inputList:
    char = findSimilarChar(rucksack)
    prioSum += charToPrio(char)

print(prioSum)

print("---------------")

def findSimilarChar3(rucksacks):
    for char in rucksacks[0]:
        if (char in rucksacks[1]) and (char in rucksacks[2]):
            return char

with open("Tag 3.txt") as file:
    initInputList = file.readlines()
    inputList = []
    for i in range(len(initInputList)//3):
        threeList = [initInputList[(i*3)].strip(),initInputList[(i*3)+1].strip(),initInputList[(i*3)+2].strip()]
        inputList.append(threeList)
print(inputList)
prioSum = 0
for rucksacks in inputList:
    char = findSimilarChar3(rucksacks)
    prioSum += charToPrio(char)

print(prioSum)
