matrixa = [[1,2],[3,4]]
matrixb = [[5,6],[7,8]]
matrixadditionresult = [[0,0],[0,0]]
matrixsubstractionresult = [[0,0],[0,0]]
matrixmultiplicationresult = [[0,0],[0,0]]

for i in range(0,2):
    for j in range(0,2): 
        matrixadditionresult[i][j] = matrixa[i][j] + matrixb[i][j]
        matrixsubstractionresult[i][j] = matrixa[i][j] - matrixb[i][j] 

for i in range(0,2):
    for j in range(0,2): 
        for k in range(0,2): 
            matrixmultiplicationresult[i][j] = (matrixa[i][k] * matrixb[k][j]) + matrixmultiplicationresult[i][j]


print(matrixadditionresult)
print(matrixsubstractionresult) 
print(matrixmultiplicationresult) 