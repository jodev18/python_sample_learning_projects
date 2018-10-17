#factorial

inputval = int(input("Enter a number to get its factorial:"))

factorial_val = 1
for xx in range(1,inputval+1):
    factorial_val *= xx

print(factorial_val)