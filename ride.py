print("select your ride:")
print("1. Bike")
print("2. Car")
#take input number from 1 or 2
#select your ride
ride = int(input("Enter your choice (1 or 2): "))
# if user selects bike
if ride == 1:
    print ("what type of bike?")
    print("1. scooty\n")
    print("2. motorcycle\n")
    bike_type = int(input("Enter your choice (1 or 2): "))
    if bike_type == 1:
        print("You have selected Scooty. Enjoy your ride!")
    elif bike_type == 2:
        print("You have selected Motorcycle. Enjoy your ride!")
    

    if ride == 2:
        print ("what type of car?")
        print("1. honda \n")
        print("2. Sedan\n")
        car_type = int(input("Enter your choice (1 or 2): "))
        if car_type == 1:
            print("You have selected Honda. Enjoy your ride!")
        elif car_type == 2:
            print("You have selected Sedan. Enjoy your ride!")
        else:
            print("Invalid choice for car type.")




