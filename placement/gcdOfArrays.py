n = int(input("Enter the number of arrays: "))
arr = []

def findGcd(s):
    s = list(map(int, s.split(" ")))
    
    m = min(s)

    if m==0:
        return 0
    
    ans = 0

    for i in range(m, 1, -1):
        div = True
        for j in s:
            if j%i!=0:
                div = False
        if div == True:
            ans = i
            break
    
    return ans

for i in range(n):
    arr.append(input(f"Input array:"))

for i in range(n):
    print(findGcd(arr[i]))