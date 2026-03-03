matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("element at row 0, colum 3:",matrix[2][2])

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()