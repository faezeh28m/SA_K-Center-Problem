import random
def new_matrix(matrix):
    i=0
    j=0

    while(True):
        i = random.randint(0,2)
        j = random.randint(0,2)
        if matrix[i][j]==0:
            break
    j2=0
    for j2 in range(3):
        if(matrix[i][j2]==1):
            matrix[i][j2] = 0
            break

    i2=0
    for i2 in range(3):
        if(matrix[i2][j]==1):
            matrix[i2][j] = 0
            break
    
    matrix[i2][j2] = 1
    matrix[i][j] = 1
    return matrix

matrix=[[0, 1, 0],[1,0,0],[0,0,1]]
print(new_matrix(matrix))