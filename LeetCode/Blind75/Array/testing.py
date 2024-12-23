import time
import random

def generate_random_numbers(count, min_val, max_val):
    """Generates a list of random numbers."""
    numbers = []
    for _ in range(count):
        num = random.randint(min_val, max_val)
        numbers.append(num)
        time.sleep(0.1)  # Simulate some processing delay
    return numbers

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)

def find_primes(numbers):
    """Finds all prime numbers in a list."""
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(num)]
    return primes

def main():
    print("Starting the debugger test script...")

    # Generate random numbers
    print("Generating random numbers...")
    numbers = generate_random_numbers(10, 1, 100)
    print(f"Generated numbers: {numbers}")

    # Calculate average
    try:
        print("Calculating the average...")
        average = calculate_average(numbers)
        print(f"Average: {average}")
    except ValueError as e:
        print(f"Error: {e}")

    # Find prime numbers
    print("Finding prime numbers...")
    primes = find_primes(numbers)
    print(f"Prime numbers: {primes}")

    print("Debugger test script completed.")

if __name__ == "__main__":
    main()
