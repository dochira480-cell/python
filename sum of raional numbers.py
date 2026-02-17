# enter the value of terms
n = int(input("Enter the number of terms: "))

sum = 0 # initialize sum
i = 1 # initialize counter
while i <= n:
    sum = sum + 1/i # add the current term to the sum
    i = i + 1 # increment the counter

print ("\n sum = ", sum) # print the final sum