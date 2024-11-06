import time

# our variables
foods =  []
prices =  []
total = 0

while True:
    # first input and check it
    food = str(input("Enter the food you just bought(q to quit): "))
    if food.lower() == 'q':
        break
    if not food.isalpha():
        raise ValueError("Must be string value")
    else:
        # second input and check it
        price = float(input(f"Enter a price of the {food}: $"))
        if price < 0:
            raise ValueError("Price can not be less than 0")
        foods.append(food.capitalize())
        prices.append(price)

print("Your recipe printing")
time.sleep(3)

print("******* YOUR RECIPE *******")

# total price
total = sum(prices)
print()
# to write the input elements and their prices
for index,(foods,prices) in enumerate(zip(foods,prices),start = 1):
    print(f"Your {index}. order was {foods} and the price was {prices}$")
print()

print(f"***** OUT COME IS {total}$ *******")

