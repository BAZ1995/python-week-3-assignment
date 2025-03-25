def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after applying discount (if applicable): {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numerical values.")
