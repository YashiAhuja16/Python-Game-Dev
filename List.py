matrix = [[1,2,3,10],[4,5,6,11],[7,8,9,12]]
print (matrix)
print (len(matrix[0])) 
print (matrix[1][2])
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j])
    print("\n")

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
matrix = []

for i in range(row): 
    temp = []
    for j in range(column): 
        x = int(input("Enter your element: "))
        temp.append(x) 
    matrix.append(temp) 

print(matrix)