
foods =  []
prices =  []
total = 0

while True:
    food = str(input("Enter the food you just bought(q to quit): "))
    if food.lower() == 'q':
        break
    if not food.isalpha():
        raise ValueError("Must be string value")
    else:
        price = float(input(f"Enter a price of the {food}: $"))
        if price < 0:
            raise ValueError("Price cannot be less than 0")
        foods.append(food.capitalize())
        prices.append(price)

print("******* YOUR RECIPE *******")
total = sum(prices)
print()
for index,(foods,prices) in enumerate(zip(foods,prices),start = 1):
    print(f"Your {index}. order was {foods} and the price was {prices}$")
print()
print(f"***** OUT COME IS {total}$ *******")

