n = int(input("Enter the length of the array"))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter {i} element: ")))


print("The elements are: ")
for i in range(n):
    if i==n-1 and arr[i]>arr[i-1]:
        print(arr[i], end=" ")
    elif i==0 and arr[i]>arr[i+1]:
        print(arr[i], end=" ")
    elif(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
        print(arr[i], end=" ")