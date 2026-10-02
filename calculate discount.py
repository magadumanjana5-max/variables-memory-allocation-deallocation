def calculate_discount(purchase_amount):
	if purchase_amount < 0:
		raise ValueError("Purchase amount cannot be negative.")

	if purchase_amount >= 5000:
		discount_rate = 0.20
	elif purchase_amount >= 3000:
		discount_rate = 0.10
	else:
		discount_rate = 0.05

	discount_amount = purchase_amount * discount_rate
	return {
		"Discount amount": discount_amount,
		"Final payable amount": purchase_amount - discount_amount,
	}


try:
	purchase_amount = float(input("Enter the purchase amount in rupees: "))
	for result, amount in calculate_discount(purchase_amount).items():
		print(f"{result}: Rs. {amount:.2f}")
except ValueError as error:
	print(error if str(error) else "Please enter a valid purchase amount.")