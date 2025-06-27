# Lyric Tyler
# June 23rd, 2025
# P2LAB2_TylerLyric
# Create a dictionary for vehicles that shows the miles per gallon,
# how many miles will be driven, and how much gas is used for that distance.

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

car_name = input("Enter a car: ")

car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

miles_driven = float(input(f"How many miles will you drive the {car_name}?: "))

gallons_needed = miles_driven/car_mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")



