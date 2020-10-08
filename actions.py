def main(matrix, act, x, y): #This file is responsible for action checking, and making alterations to our tile grid
    #Please note, this function carries out the action if possible, null returned if not.
    #This function is not responsable for "investigating" if the action is worth taking
    #We are shifting TO an filled tile FROM the empty tile

    #Shallow copies our CURRENT matrix
    if act.lower()=="leftshift":
        hsl = horizontalshiftleft(matrix,x,y)
        return hsl
    elif act.lower()=="rightshift":
        hsr = horizontalshiftright(matrix,x,y)
        return hsr
    elif act.lower()=="upshift":
        vsu = verticalshiftup(matrix,x,y)
        return vsu
    elif act.lower()=="downshift":
        vsd = verticalshiftdown(matrix,x,y)
        return vsd

    #There should be no case where act is not a listed value
def horizontalshiftleft(matrix,x,y): #Left does not exist
    #Error checking
    if x > 0:
        temp = int(matrix[x-1][y])
        matrix[x-1][y] = int(matrix[x][y])
        matrix[x][y] = int(temp)
        return matrix
  #If we are going out of bound, or left shift is occupied
    else: return None

    return 1 #No need to return matricies as matricies are referred too

def horizontalshiftright(matrix,x,y):
    n = len(matrix)
    #Error checking
    if x < (n-1):
        temp = int(matrix[x+1][y])
        matrix[x+1][y] = int(matrix[x][y])
        matrix[x][y] = int(temp)
        return matrix
    else: return None
      

    return 1 #No need to return matricies as matricies are referred too

def verticalshiftdown(matrix,x,y):
    #Error checking
    n = len(matrix)
    if y < (n-1):
        temp = int(matrix[x][y+1])
        matrix[x][y+1] = int(matrix[x][y])
        matrix[x][y] = int(temp)  #If we are going out of bound, or downward shift is occupied
        return matrix
    else:return None

    return 1 #No need to return matricies as matricies are referred too

def verticalshiftup(matrix,x,y):
    if y > 0:
        temp = int(matrix[x][y-1])
        matrix[x][y-1] = int(matrix[x][y])
        matrix[x][y] = int(temp)  #If we are going out of bound, or downward shift is occupied
        return matrix
    else: return None


    return 1 #No need to return matricies as matricies are referred too
    
