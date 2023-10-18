# create variables to store user inputs
city_flight = input("Please enter the city you will be flying to (New York, Los Angeles, Chicago):\n")
num_nights = int(input("How many nights will you be staying at the hotel?\n"))
rental_days = int(input("Please enter the number of days you will be hiring a car for:\n"))

# use def function to calculate and save hotel cost, set at R1500 a night
def hotel_cost(num_nights):
    return num_nights * 1500

# use def function to work out plane cost, use if elif and else statements.
def plane_cost(city_flight):
    if city_flight == "New York":
        return 15000
    elif city_flight == "Los Angeles":
        return 18000
    elif city_flight == "Chicago":
        return 14000
    else:
        return 10000  # used else statement for and other city entered, set at a default price of R10000

# use def function to calculate the car rental at R500 a day
def car_rental(rental_days):
    return rental_days * 500

# use def function to calculate and save holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# create variables to store final calculations
total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_car_rental_cost = car_rental(rental_days)
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental_cost)

# print each statement seperately to make it more readable
print("\nHoliday Breakdown:")
print("City: " + city_flight)
print("Number of nights in the hotel: " + str(num_nights))
print("Number of days for car rental: " + str(rental_days))
print("Hotel cost: R" + str(total_hotel_cost))
print("Plane cost: R" + str(total_plane_cost))
print("Car rental cost: R" + str(total_car_rental_cost))
print("The total cost of your holiday is: R" + str(total_holiday_cost))
