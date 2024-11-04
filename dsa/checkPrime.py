def isPrime(i):
    if i == 1:
        return True
    elif i<2:
        return False
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            return False
    return True

n = int(input("Enter number to check prime: "))

print(f"number is {isPrime(n)}")