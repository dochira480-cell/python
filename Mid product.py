num = int(input("enter a number:"))
t = num
numlen = 0
while t>0:
   numlen = numlen + 1
   t = int(t/10)
if numlen >= 4: #condition 1
   numlen = int(numlen/2)
   chk = 0
   while numlen > 0: #literate loop
    rem = num%10
    if chk == numlen: #nested condition
        midone = rem
    elif chk == numlen - 1:
        midtwo = rem
    num = int(num/10)
    chk = chk + 1
    prod = midone * midtwo
    print("\n Product of middigits is" + str(midone) + " * " + str(midtwo) + " = " , prod)