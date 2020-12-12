nums = int(input())
arr = []

for i in range(nums):
    arr.append(int(input()))

find = int(input())
end = 0
for i in arr:

    if i == find:

        end += 1

print(end)
