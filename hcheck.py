def main(matrix, destination_matrix):
    #So, hcheck will be returning our h1, and our h2 (n) to the main program
    #First lets start with h1, this returns only the amount of msiplaced tiles, it should be eaiser to calculate

    #FINDING H1(n), step through and search
    h1 = 0
    w = len(matrix[0])

    for x in range (0, w):
        for y in range(0, w):
            if matrix[x][y] != destination_matrix[x][y]: ++h1

    #H1 should be properly calculated by the above function
    #H2 is a bit trickier to calcualte
    ##I believe the simplest way, although not very efficent, is to check the "coordinates" against eachother, and go off that

    h2 = 0
    for x in range (0, w):
        for y in range(0, w):
            xwant, ywant = want(0, destination_matrix, w)
            h2+= coordcheck(x,y,xwant,ywant)


    return [h1, h2]#We now have our h1 and h2 values, obviously we want to get these as close to zero as possible, and end
    #with both numbers being zero
            

def want (num, dest, w):
    for x in range (0, w):
        for y in range(0, w):
            if dest[x][y] == num: return x, y #There should be no case where a number cannot be found

def coordcheck (xat, yat, xwant, ywant): #Simple function, compare where we are at, and be done
    xdif = abs(xat - xwant)
    ydif = abs(yat - ywant)
    #Now we have the absolute value of how many times we have to shift horizontally, or vertically, just add and return
    return (xdif + ydif)
