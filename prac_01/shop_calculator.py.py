DISCOUNT = 0.1

total_price_of_items = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))

    total_price_of_items += item_price
if total_price_of_items > 100:
    discount_amount = total_price_of_items * DISCOUNT
    total_price_of_items -= discount_amount

print(f"Total price for {number_of_items} items is ${total_price_of_items:.2f}")
