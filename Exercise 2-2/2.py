from decimal import Decimal

book = Decimal(24.95)
discount_percentage = Decimal(0.4)
shipping = Decimal(3.0)
reduced_shipping = Decimal(0.75)
quantity = 60

discount = book * discount_percentage
wholesale_price = book - discount
total_books = wholesale_price * quantity
total_shipping = shipping + (reduced_shipping * (quantity - 1))

cost = total_books + total_shipping

print(f'${cost:.2f}')

# cost = 24.95 * 0.6 * 60 + 0.75 * (60 - 1) + 3
# print(round(cost, 2))
