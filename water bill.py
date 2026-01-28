# take input of number of units consumed by the user
units = int(input("Enter the number of units consumed: "))
# calculate the water bill based on the units consumed
#then calclate bill and surcharge
# surcharge is the tax value

#check of units less than 50
if units <= 50:
    amount = units * 2.60
    surcharge = 25
#check of units less than a 100
elif units <= 100:

    amount = (130 + (units -50)) *3.25
    surcharge = 35
# check of units less than 200
elif units <= 200:
    amount = (162 + 162.5 + (units -100) *5.26)
    surcharge = 45
#check for all other cases 
else:
    amount = (162 + 162.5 + 526 + (units -200) *8.45)
    surcharge = 75
total_bill = amount + surcharge
print("The total water bill is: ", total_bill)