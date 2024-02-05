def is_square_number(number):
    """
    Check if a number is a square number.

    Args:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is a square number, False otherwise.
    """
    if number < 0:
        return False
    root = int(number ** 0.5)
    return root * root == number

# Example usage
num = 16
print(f"{num} is a square number: {is_square_number(num)}")
