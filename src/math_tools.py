"""
Math Tools Module
A collection of useful mathematical functions and utilities.
"""

import math
from typing import List, Union


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number (0-indexed).

    Args:
        n: Position in Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: Integer to check

    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Greatest common divisor of a and b
    """
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Least common multiple of a and b
    """
    return abs(a * b) // gcd(a, b) if a and b else 0


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        Arithmetic mean

    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        Median value

    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def standard_deviation(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        Standard deviation

    Raises:
        ValueError: If the list is empty or has only one element
    """
    if len(numbers) < 2:
        raise ValueError("Standard deviation requires at least 2 numbers")

    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)


def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """
    Calculate base raised to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base ** exponent
    """
    return math.pow(base, exponent)


def sqrt(n: Union[int, float]) -> float:
    """
    Calculate the square root of a number.

    Args:
        n: Non-negative number

    Returns:
        Square root of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)


def is_perfect_square(n: int) -> bool:
    """
    Check if a number is a perfect square.

    Args:
        n: Integer to check

    Returns:
        True if n is a perfect square, False otherwise
    """
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n


def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        x1: X-coordinate of first point
        y1: Y-coordinate of first point
        x2: X-coordinate of second point
        y2: Y-coordinate of second point

    Returns:
        Euclidean distance between the points
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def quadratic_formula(a: float, b: float, c: float) -> tuple:
    """
    Solve a quadratic equation ax^2 + bx + c = 0.

    Args:
        a: Coefficient of x^2
        b: Coefficient of x
        c: Constant term

    Returns:
        Tuple of solutions (x1, x2) or (x,) if one solution, or empty tuple if no real solutions

    Raises:
        ValueError: If a is 0 (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("'a' cannot be 0 in a quadratic equation")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return ()  # No real solutions
    elif discriminant == 0:
        return (-b / (2 * a),)  # One solution
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return (x1, x2)


def percentage(part: Union[int, float], whole: Union[int, float]) -> float:
    """
    Calculate what percentage 'part' is of 'whole'.

    Args:
        part: The part value
        whole: The whole value

    Returns:
        Percentage value

    Raises:
        ValueError: If whole is 0
    """
    if whole == 0:
        raise ValueError("Cannot calculate percentage when whole is 0")
    return (part / whole) * 100


def clamp(value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]) -> Union[int, float]:
    """
    Clamp a value between a minimum and maximum.

    Args:
        value: Value to clamp
        min_value: Minimum allowed value
        max_value: Maximum allowed value

    Returns:
        Clamped value
    """
    return max(min_value, min(max_value, value))
