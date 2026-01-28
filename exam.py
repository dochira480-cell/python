#take input of student that he can attend exam or not
medical_cause = input("Do you have a medical cause? (yes/no): ")
attendence_percentage = float(input("Enter your attendance percentage: "))


# Checking the user input predicting output accordingly
if medical_cause.lower() == 'yes':
    print("You are allowed to sit in the exam due to medical cause.")
elif attendence_percentage >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("You are not allowed to sit in the exam.")
