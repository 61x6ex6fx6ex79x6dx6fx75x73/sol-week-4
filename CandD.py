x = int(input())

arr = []

for i in range(x):
    input()
    for j in map(int, input().split(" ")):
        arr.append(j)

def printA(ac):

    for i in ac:

        print(i, end=" ")

    print()

printA(sorted(arr))
