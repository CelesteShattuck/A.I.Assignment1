#Okay, this function, I believe will be kinda like the universal investigation function
#We will make copies of our main matrix, and conduct an investigation of the moves we could make
#What I mean by this, is that we will copy, make a move on the copy, and check our huristics
#What we do then is compare the two, three, or four (because in this problem, there is that many) possible moves to make
#at a given point
#matrix, our current matrix, x, y coordinates of our BLANK SPACE
import actions
import hcheck
def main(matrix, x, y, dest):
    #So our actions actually already do our error checking, so because it is taken care of there, we don't need to worry here
    act = ["leftshift", "rightshift", "upshift", "downshift"]

    #Above are are our actions we can take constrained to require adjacency 
    #We will now step through our matrix and see which one is the smallest heursitic, meaning more greedy
    ourPos = []
    for i in range (0,4):
        if i == 0: ourPos.append(actions.main(matrix, act[i], x,y)) #leftshift
        elif i == 1: ourPos.append(actions.main(matrix, act[i], x,y)) #rightshift
        elif i == 2: ourPos.append(actions.main(matrix, act[i], x,y)) #upshift
        elif i == 3: ourPos.append(actions.main(matrix, act[i], x,y)) #downshift
    #we now step through all our possible actions, and have all possible actions

    #Okay, now we have our "child" for a given state, now we walk through to see what would be best
    heurisics = [] #Note, actions already uses a "deepcopy" so our original function has not been changed
    for i in range (0,4):
        if i == 0: heurisics.append(hcheck.main(matrix, dest)) #leftshift
        elif i == 1: heurisics.append(hcheck.main(matrix, dest)) #rightshift
        elif i == 2: heurisics.append(hcheck.main(matrix, dest)) #upshift
        elif i == 3: heurisics.append(hcheck.main(matrix, dest)) #downshift


    #Now we can return our child maricies and our heurisics to the calling main


    return ourPos, heurisics
