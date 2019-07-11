import numpy as np
import csv
def readm(fname='A.csv'):
    f = open(fname,'r')
    A = []
    b = []
    for line in f.readlines():
        A.append([float(x) for x in line.strip(',')])
        b.append([float(y) for y in line.strip(',')])
    f.close()
    return A,b
def matmul(A,b):
    m,n = len(A) , len(b[0])
    J = len(A[0]) #A - m*j #b - j*n
    if len(A[0])==len(b):
        C = [ [0]*n for i in range(m) ]
        for r in range(m):
            for c in range(n):
                C[r][c] = sum([float(A[r][j])*float(b[j][c]) for j in range(J) ])
        return C
    return []
