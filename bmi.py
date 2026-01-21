height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / ((height / 100) ** 2)
print ("your BMI is :", bmi)
if bmi < 18.5:
    print ("You are underweight")
elif 18.5 <= bmi < 24.9:
    print ("You have a healthy weight")
elif 25 <= bmi < 29.9:
    print ("You are overweight")
elif 30 <= bmi < 34.9:
    print ("You are severely overweight")
elif 35 <= bmi < 39.9:
    print ("You are obese")
else:
    print ("You are severely obese")