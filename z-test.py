table_1 = [
    [0],
    [9, 0],
    [17, 9, 0]]
table_2 = [
    [0],
    [10, 0],
    [0, 10, 0]]

def D(i , k):
    if( i > 2 or k > 2 or i <0 or k < 0):
        return False
    elif i > k:
        return table_1[i][k]
    else:
        return table_1[k][i]

def W(j , s):
    if( j > 2 or s > 2 or j < 0 or s < 0):
        return False
    elif j > s:
        return table_2[j][s]
    else:
        return table_2[s][j]

def x(i , j , k , s , matrix):
    x = matrix[i][j] * matrix[k][s]
    return x

def z(matrix):
    sum = 0
    
    for i in range(3):
        for j  in range (3):
            for k in range (3):
                for s in range (3):
                    sum += D(i , k)*W(j , s)*x(i , j , k , s , matrix)
                    print('i=',i,'j=',j,'k=',k,'s=',s,'sum=',sum)

    return sum


    
matrix=[[1, 0, 0],[0,1,0],[0,0,1]]
print(z(matrix))

