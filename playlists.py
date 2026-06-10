L = [1, 2, 3, 4, 5]
print("original list: ", L)

count = 0

for i in L:
    count += 1

avg = count / len(L)

print("sum of the list: ", count)
print("average of the list: ", avg)

L.sort()

print("Smaller number in the list: ", L[0])

print("Larger number in the list: ", L[-1])

