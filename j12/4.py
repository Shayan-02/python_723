def sum_numbers(a: int, b: int) -> int:
    """
    Get two number and return sum of them.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: sum of a and b
    """
    c = a + b
    return c

# call function
a = input()
print(sum_numbers(5, 6))