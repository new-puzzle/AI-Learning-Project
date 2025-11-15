"""
Examples demonstrating the use of math_tools module.
"""

from src.math_tools import (
    factorial, fibonacci, is_prime, gcd, lcm,
    mean, median, standard_deviation,
    power, sqrt, is_perfect_square,
    distance_2d, quadratic_formula,
    percentage, clamp
)


def main():
    print("=" * 60)
    print("Math Tools Examples")
    print("=" * 60)

    # Number Theory
    print("\n--- Number Theory ---")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"10th Fibonacci number: {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 20 prime? {is_prime(20)}")
    print(f"GCD of 48 and 18: {gcd(48, 18)}")
    print(f"LCM of 12 and 15: {lcm(12, 15)}")

    # Statistics
    print("\n--- Statistics ---")
    numbers = [10, 20, 30, 40, 50]
    print(f"Numbers: {numbers}")
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Standard Deviation: {standard_deviation(numbers):.2f}")

    # Powers and Roots
    print("\n--- Powers and Roots ---")
    print(f"2 to the power of 8: {power(2, 8)}")
    print(f"Square root of 144: {sqrt(144)}")
    print(f"Is 64 a perfect square? {is_perfect_square(64)}")
    print(f"Is 50 a perfect square? {is_perfect_square(50)}")

    # Geometry
    print("\n--- Geometry ---")
    print(f"Distance between (0,0) and (3,4): {distance_2d(0, 0, 3, 4)}")
    print(f"Distance between (1,2) and (4,6): {distance_2d(1, 2, 4, 6):.2f}")

    # Algebra
    print("\n--- Algebra ---")
    print("Solving x^2 - 5x + 6 = 0:")
    solutions = quadratic_formula(1, -5, 6)
    print(f"Solutions: x = {solutions[0]}, x = {solutions[1]}")

    print("\nSolving 2x^2 + 4x + 2 = 0:")
    solutions = quadratic_formula(2, 4, 2)
    print(f"Solutions: x = {solutions[0]}")

    # Utilities
    print("\n--- Utilities ---")
    print(f"What percentage is 25 of 200? {percentage(25, 200)}%")
    print(f"Clamp 150 between 0 and 100: {clamp(150, 0, 100)}")
    print(f"Clamp -10 between 0 and 100: {clamp(-10, 0, 100)}")
    print(f"Clamp 50 between 0 and 100: {clamp(50, 0, 100)}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
