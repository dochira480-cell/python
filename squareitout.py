def SquaredValues(beg, end):
    lst = []
    for i in range(beg, end + 1):
        lst.append(i ** 2)

    lst_even = []
    lst_odd = []
    for i in lst:
        if i % 2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)

    print("List of even squared values: ", lst_even)
    print("List of odd squared values: ", lst_odd)

beg = int(input("Enter the beginning of the range: "))
end = int(input("Enter the end of the range: "))
SquaredValues(beg, end)
