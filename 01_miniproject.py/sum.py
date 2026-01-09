'''
sum(1) = 1
sum(2) = 2 + 1
sum(3) = 3 + 2 + 1
sum(n) = 1 + 2 + 3 + ... + (n-1) + n
sum(n) = n + sum(n-1)
'''
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

input_number = int(input("your number : "))
result = sum(input_number)
print(result)  