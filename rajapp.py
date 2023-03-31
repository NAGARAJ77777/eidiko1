def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average is:", average)

