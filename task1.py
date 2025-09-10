# Discount function with input prompts
def discount(price, category):
	if category == "student":
		return price * 0.9 if price > 1000 else price * 0.95
	return price * 0.85 if price > 2000 else price

price = float(input("Enter the price: "))
category = input("Enter the category (student/other): ").strip().lower()
print(f"Discounted price: {discount(price, category)}")
