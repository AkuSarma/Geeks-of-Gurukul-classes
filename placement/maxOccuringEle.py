# first approach
# less time more storage
arr = list(map(int, input("Enter the array: ").split()))
dic = {}

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# print(dic)
max = 0

for i in dic:
    if dic[i]>max:
        max = i
    
print(max)

# second approach
# less storage more time .
n = None
maxCount = 0
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if i!=j:
            if arr[i] == arr[j]:
                count += 1
    if count>maxCount:
        n = arr[i]

print(n)
