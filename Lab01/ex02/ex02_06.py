input_str = input("Enter X,Y: ")
dimensions = [int(x) for x in input_str.split(",")]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)
# The code above creates a 2D list (matrix) with dimensions specified by the user, where each element is the product of its row and column indices. It then prints the resulting matrix.