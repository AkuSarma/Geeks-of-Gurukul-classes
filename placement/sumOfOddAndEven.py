lst = [1,3,5,9,14,16]
odd = 0
even = 0

for i in lst:
    if i%2==0:
        even+=i
    else:
        odd+=i

if even>odd:
    print("Even")
else:
    print("Odd")