a = int(input("Enter value of a: "))
s = input("Enter the string: ")

s = list(s)
sum = 0
for i in s:
    # print(ord(i) - ord('a'))
    cSum = a + (ord(i) - ord('a'))
    # print(cSum)
    sum += cSum

print(sum)