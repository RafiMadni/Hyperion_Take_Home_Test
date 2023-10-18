# Create a variable list to store menu items
menu = ["Coffee", "Latte", "Mocha", "Tea"]

# Create a 'stock' dictionary using curly bracket method
stock = {"Coffee": 40,
        "Latte": 20,
        "Mocha": 25,
        "Tea": 50}

# Create a 'price' dictionary
price = {"Coffee": 50,
         "Latte": 70,
         "Mocha": 75,
         "Tea": 40}

# calculate the sum using the sum function, use list comprehension to calculate each item worth
total_stock_worth = sum(stock[item] * price[item] for item in menu)

print("Total stock worth:", total_stock_worth)