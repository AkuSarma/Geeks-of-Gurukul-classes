s = input("Enter the string: ")

sLen = len(s)
possible = 0

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

    # if n==1:
    #     return 1
    
    # return n * fact(n-1)

def isPrime(i):
    if i == 1:
        return True
    elif i<1:
        return False
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            return False
    return True

def checkPossibleSubstring(n):
    if n < 0 or n > sLen:
        return 0
    # count = 0
    # for i in range(sLen - n + 1):
    #     substring = s[i:i+n]
    #     print(substring)
    #     if len(substring) == n:
    #         count += 1
    # return count

    # Combinations: (nCr = n! / [r!((n-r)!)]
    # print(n)
    # print(fact(n))
    # print(fact(sLen))
    return fact(sLen) // (fact(n) * fact(sLen - n))

for i in range(1, sLen+1):
    if isPrime(i):
        possible += checkPossibleSubstring(i)

print(possible)