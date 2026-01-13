# take marks as input from user
print("Enter marks obtained in 4 subjects: ")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
history = int(input("History: "))
# calculate total marks
total_marks = math + science + english + history
# calculate percentage
percentage = (total_marks / 400) * 100

print(end="percentage marks: ")
print(percentage)