#In this function, we will begin doing our tests, and our steps, we will continue to move about, and
#hopefully find a path to a solution if one exists
import actions
import generate
import investigate
import findEmpty
def main (puzzleSize):
    solveMe, destination = generate.main(puzzleSize)
    return solveMe, destination

puzzleSize = 0
while puzzleSize != 8 and puzzleSize != 15 and puzzleSize != 24:
    try:
        puzzleSize = int(input("8, 15, 24, are your options. Please enter the puzzle size: "))  
    except (ValueError, SyntaxError, NameError):
       print("Not a valid number! Try again. (8, 15, 24) \n")
       puzzleSize = 0
       continue
       



toSolve, dest = main(puzzleSize)
print (dest)
#Now we have what OUR puzzle is, and we have a what matrix we want to achieve at the end

y, x = findEmpty.main(toSolve)

newMat, heur = investigate.main(toSolve, x, y, dest)


print("Our new possabilities are: ")
j = 0 #Heur
for i in range(0, len(newMat)):
    if (newMat[i] is not None):
        print(newMat[i])
        print(heur[j])
        ++j

bestIndex = -1
bestScore = -1
for i in range(0, j):
    if(heur[i][0] + heur[i][1] > bestScore):
        bestScore = heur[i][0] + heur[i][1]
        bestIndex = i

#print("It would be best to check this matrix next")
# print(newMat[bestIndex])