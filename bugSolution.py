def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after removing non-numeric elements
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) 
print(f"The average of an empty list is: {average_empty}")

# Example with non-numeric values
my_numbers_with_string = [10, 20, '30']
average_with_string = calculate_average(my_numbers_with_string)
print(f"The average is: {average_with_string}")

my_numbers_with_mixed_types = [10, 20, 30, 'a', 40.5]
average_mixed = calculate_average(my_numbers_with_mixed_types)
print(f"The average is: {average_mixed}") 