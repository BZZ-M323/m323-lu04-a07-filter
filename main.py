def filter_even_numbers(numbers):
    """
    Filtert die geraden Zahlen aus der gegebenen Liste.
    Args:
    - numbers (list): Eine Liste von Zahlen.
    Returns:
    - even_numbers_list: Eine Liste der geraden Zahlen.
    """
    # Ihr Code hier
    return even_numbers_list


if __name__ == '__main__':
    numbers = list(range(1, 51))
    even_numbers = filter_even_numbers(numbers)
    print(list(even_numbers))