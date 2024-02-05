def calculate_gst(amount):
    """
    Calculate GST (Goods and Services Tax) for a given amount.
    
    Args:
    amount (float): The total amount for which GST needs to be calculated.
    
    Returns:
    float: The GST amount calculated based on the given amount.
    """
    gst_rate = 0.18  # GST rate is 18%
    gst_amount = amount * gst_rate
    return gst_amount

def calculate_income_tax(income):
    """
    Calculate Income Tax for a given income.
    
    Args:
    income (float): The total income for which Income Tax needs to be calculated.
    
    Returns:
    float: The Income Tax amount calculated based on the given income.
    """
    tax_rate = 0.15  # Tax rate is 15%
    tax_amount = income * tax_rate
    return tax_amount

# Example usage
total_amount = 1000.0
gst = calculate_gst(total_amount)
print(f"GST for amount {total_amount} is: {gst}")

total_income = 50000.0
income_tax = calculate_income_tax(total_income)
print(f"Income Tax for income {total_income} is: {income_tax}")
