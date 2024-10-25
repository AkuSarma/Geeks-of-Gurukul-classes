n = int(input("length of array: "))
s = int(input("number to equal: "))
arr = []
count = 0
for i in range(n):
    arr.append(int(input(f"Enter {i} element")))

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == s:
            count += 1
            print(f"{arr[i]} {arr[j]}")

print(f"Total such pairs are: {count}")