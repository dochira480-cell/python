#taking total amount as imput from user
amount = int(input("Enter amount for withdraw"))
#calculating the number of notes 
note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = (amount % 100) % 50 // 10

print("notes of 100 rupees :", note_1)
print("notes of 50 rupees :", note_2)
print("notes of 10 rupees :", note_3)