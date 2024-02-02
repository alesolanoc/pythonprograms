def print_2d_list_elements(arr):
    """
    Print 2D list elements using nested for loops.

    Args:
    arr (list): A 2D list containing elements to be printed.

    Returns:
    None
    """
    for row in arr:  # Iterate through each row in the 2D list
        for elem in row:  # Iterate through each element in the row
            print(elem, end=" ")  # Print the element followed by a space
        print()  # Move to the next line after printing all elements in the row


# Example usage
my_2d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_2d_list_elements(my_2d_list)
