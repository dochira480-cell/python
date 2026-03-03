# take input from the user
lower = int(input("enter the lower range:"))
upper = int(input("enter the upper range:"))
print("the prime numbers between", lower, "and", upper, "are:")
# literate loop between lower and upper
for num in range(lower, upper + 1):
    # check for prime number
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
            else:
                print(num)