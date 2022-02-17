#Faezeh Movahedi
#Fatemeh Dinani
#Tamrin 3 AI

import random
from math import e #for e number in SA function
import copy

with open('table1.txt', 'r') as f:
    table_1 = [[int(num) for num in line.split(',')] for line in f]

with open('table2.txt', 'r') as f:
    table_2 = [[int(num) for num in line.split(',')] for line in f]

def D(i , k):
    if( i > 19 or k > 19 or i < 0 or k < 0):
        return False
    elif i > k:
        return table_1 [i][k]
    else:
        return table_1 [k][i]

def W(j , s):
    if( j > 19 or s > 19 or j < 0 or s < 0):
        return False
    elif j > s:
        return table_2[j][s]
    else:
        return table_2[s][j]

# #for check D and W function:
# Dij = D (i-1 , j-1):
#     Because the values ​​of the rows and columns of the matrix in Python are one less than the normal state of the tables 
# D11= D(0,0)
# D26=D(1,5)
# D103=D(9,2)
# D201=D(19,0)
# D211=D(20,0)
# D2020=D(19,19)

# print('D11 = ', D11)
# print('D26 = ', D26)
# print('D103 = ', D103)
# print('D201 = ', D201)
# print('D2020 = ', D2020)

#Wij = D (i-1 , j-1):
#     Because the values ​​of the rows and columns of the matrix in Python are one less than the normal state of the tables 
# W11= W(0,0)
# W26=W(1,5)
# W103=W(9,2)
# W201=W(19,0)
# W2020=W(19,19)

# print('w11 = ', W11)
# print('w26 = ', W26)
# print('w103 = ', W103)
# print('w201 = ', W201)
# print('w2020 = ', W2020)


def x(i , j , k , s , matrix):
    x = matrix[i][j] * matrix[k][s]
    return x


def z(matrix):
    sum = 0

    for i in range(20):
        for j in range (20):
            for k in range (20):
                for s in range (20):
                    sum += D(i , k)*W(j , s)*x(i , j , k , s , matrix)
    
    return sum


def random_matrix():
    rm = [] #random matrix
    reservation = []

    for i in range (20):
        rr = [] #random row of matrix
        while True:
            n = random.randint(0,19)
            if n not in reservation:
                break
        reservation.append(n)

        for j in range (20):
                if j == n:
                    rr.append(1)
                elif j != n:
                    rr.append(0)
        
        rm.append(rr)
    
    return rm


#for check sigma (i=0 to 20) xi,j = 1 and sigma (j=0 to n) xi,j =1 
def check_random_matrix(random_matrix):
    
    for i in range (20):
        sum = 0
        for j in range(20):
            sum += random_matrix[i][j]
        if sum != 1:
            return False
        
    for j in range (20):
        sum = 0
        for i in range(20):
            sum += random_matrix[i][j]
        if sum != 1:
            return False

    return True   


def new_matrix(matrix):

    i=0
    j=0

    while(True):
        i = random.randint(0,19)
        j = random.randint(0,19)
        if(matrix[i][j]==0):
            break
    
    """
    The following two loops have two purposes:
    1) Zero the ones that should be zero
    2) Find the zero that should become one with i2,j2
    """
    j2=0
    for j2 in range(20):
        if(matrix[i][j2]==1):
            matrix[i][j2] = 0
            break

    i2=0
    for i2 in range(20):
        if(matrix[i2][j]==1):
            matrix[i2][j] = 0
            break
    
    matrix[i2][j2] = 1
    matrix[i][j] = 1
    return matrix


def print_matrix(matrix):
    for i in range(20):
        print (matrix[i])



def SA(matrix , T):
    current = matrix
    print('Initial state with cost = ', z(current) ,'is :')
    print_matrix(current)

    i = 0
    while(True): 

        print ('\n********************************************************\nWe are in the ' , i ,'st iteration ')
        if T == 0:
            print ('\nThe SA algorithm is over :)))))')
            return current

        z_current = z(current)
        print('z current state = ' , z_current) 

        copy_current = copy.deepcopy(current)
        next_matrix = new_matrix(copy_current)

        if(next_matrix == current):
            print(' is equal')

        z_next = z(next_matrix)
        print('z next state = ' , z_next) 

        delta_z = z_current - z_next
        print('delta_z(z curent state - z next state) = ' , delta_z) 

        if delta_z > 0:
            print('\ndelta_z > 0 so the next state is better than the current state ')
            current = next_matrix
            print (':))) The current state has changed in T = ' , T ,'to good state')
        else:
            print('\ndelta_z < 0 so the next state is worse than the current state ')
            random_num = random.random()
            p = e ** (delta_z / T)
            if random_num < p :
                next_matrix_copy = next_matrix
                current = next_matrix_copy
                print (':)) The current state has changed in T = ' , T , 'to bad state with:\nprobility = ' , p , '\nrandom_number = ' , random_num)

            else:
                print (':(( The current state has NOT changed in T = ' , T , 'to bad state with:\nprobility = ' , p , '\nrandom_number = ' , random_num)
        
        i += 1    
        T = T - 1


# #for check random matrix function:
# ##with check_random_matrix you can check sigma (i=0 to 20) xi,j = 1 and sigma (j=0 to n) xi,j =1 
# random_matrix = random_matrix()
# print(random_matrix)

SA = SA(random_matrix() , 150)
print('\nGoal state with cost = ', z(SA) ,'is :')
print_matrix(SA)






    











