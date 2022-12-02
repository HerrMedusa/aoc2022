def pointsForShape(shape):
    match shape:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
    
def pointsForOutcome(opp,you):
    match you:
        case "X":
            you = "A"
        case "Y":
            you = "B"
        case "Z":
            you = "C"
    
    match (opp,you):
        case (opp,you) if (opp == you):
            return 3
        case ("A","B"):
            return 6
        case ("B","C"):
            return 6
        case ("C", "A"):
            return 6
        case _:
            return 0
        

def howMuchPointsDoIGet(opp,you):
    return pointsForShape(you) + pointsForOutcome(opp,you)

with open("Tag 2.txt") as file:
    inputList = [line.split(" ") for line in file.read().splitlines()]
    result = 0
    for line in inputList:
        (opp,you) = (line[0],line[1])
        result += howMuchPointsDoIGet(opp,you)
print(result)


def whatDoYouDo(opp,strat):
    match strat:
        case "X":
            match opp:
                case "A":
                    return "Z"
                case "B":
                    return "X"
                case "C":
                    return "Y"
        case "Y":
            match opp:
                case "A":
                    return "X"
                case "B":
                    return "Y"
                case "C":
                    return "Z"
        case "Z":
            match opp:
                case "A":
                    return "Y"
                case "B":
                    return "Z"
                case "C":
                    return "X"

with open("Tag 2.txt") as file:
    inputList = [line.split(" ") for line in file.read().splitlines()]
    result = 0
    for line in inputList:
        opp = line[0]
        you = whatDoYouDo(opp,line[1])
        result += howMuchPointsDoIGet(opp,you)
print(result)
