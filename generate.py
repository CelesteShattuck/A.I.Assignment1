import random
def main(size):
    solve_me = [] #Solve me will be a n by n matrix
    dest = [] #Destinaton matrix
    n = 0 # N will be the size of the array 8 = 3x3 15 = 4x4, 25 = 5x5
    if size == 8: n = 3
    elif size == 15: n = 4
    elif size == 24: n = 5
    else: return -1
    #The above lines determins which puzzle type we will be using, 8 is 3x3 for 9 squares, the rest follow the same pattern
    #Although possibly unneeded, -1 is our default case, if generate returns -1, there has been an error

    #The following lines will be our loop that generates random puzzles
    #The way our algorithm will work, is that we will make one, check it, and if it's solveable, we will 
    #add that matrix to the test files so we can use real solveable matrix instead of relying on randomly generated ones

    used = [] #array to store numbers in use
    for x in range(0,n):
        actualSub = []
        for y in range(0,n):
            check = random.randint(0, size)
            while check in used:
                check = random.randint(0, size)
            used.append(check)
            actualSub.append(check)
        solve_me.append(actualSub)
    
    #At this point we should have an nxn matrix filled with random numbers except the last one, which is zero
    #Zero is currently our indicator as our "blank" mark
    # we do indeed generate a random puzzle
    # print(solve_me)

    count = 1
    #For added simplicity, I will also return the destination matrix for the simplicity
    for x in range(0,n):
        actualSub = []
        for y in range(0,n):
            actualSub.append(count)
            count+=1
        dest.append(actualSub)
    
    return solve_me, dest