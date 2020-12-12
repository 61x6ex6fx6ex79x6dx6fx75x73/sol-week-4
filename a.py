
matrix = []
ele = int(input())

for i in range(ele):
    matrix.append(input())

num = 0
prefix = ""
for i in range(len(matrix[0])):

    currentWorkingChar = matrix[num][i]

    for j in range(ele):

        if currentWorkingChar != matrix[j][i]:

            if prefix:
                print(prefix)
            else:
                print("no common prefix")

            quit()

        else:
            if j == ele-1:
                prefix += matrix[j][i]

    num+=1
