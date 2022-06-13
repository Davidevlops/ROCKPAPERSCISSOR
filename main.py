import random
import string
import winsound
gameDict = {"R": 0, "S": 1, "P": 2}
gameDictKeys = list(gameDict.keys())

# if you subtract any two from each other and the answer is 1 then the lower one wins
# otherwise the higher one wins


def deternineWinner(playersNumber, computerNumber):
    difference = playersNumber-computerNumber
    if(difference > 0):
        return 0 if (difference == 2) else 1
    return 1 if (difference == -2) else 0


def playGame():
    playerOption = input(
        "PLease Enter any of Rock(R), Sciscors(S) or Paper(P)")
    capitalizedPlayerOption = playerOption.capitalize()
    if str(gameDict[capitalizedPlayerOption]).isnumeric():
        print("You can only enter any of R, S, or P")
    playerOptionIntValue = int(gameDict[capitalizedPlayerOption])
    remainderOfPlayerInput = playerOptionIntValue % 3
    print(gameDictKeys)
    computerOption = random.choice(gameDictKeys)
    print("Computer choice", computerOption)
    remainderOfComputerInput = gameDict[computerOption] % 3
    if (remainderOfPlayerInput == remainderOfComputerInput):
        print("You had same input as computer so we will goo for a rerun.")
        return playGame()
    else:
        return deternineWinner(remainderOfPlayerInput, remainderOfComputerInput)


numberOfRounds = input("Provide the number off rounds each person will have")
if str(numberOfRounds).isnumeric():
    outcomes = [0, 0]
    for sss in range(int(numberOfRounds)):
        outcomes[playGame()] += 1
    print("Outcome: ", outcomes)
else:
    print("We need numeric input")

#   def runprogram():
#     if input("R") and random.choice("S"):
#      print("You won")
#     elif input("S") and random.choice("R"):
#         print("Computer won")
#     if input("R") and random.choice("P"):
#      print("You won")
#     elif input("P") and random.choice("R"):
#      print("Computer won")
#     if input("S") and random.choice("P"):
#      print("You won")
#     elif input("P") and random.choice("S"):
#      print("Computer won")
#     if input(("")) == random.choice(""):
#         print("Computer won")
