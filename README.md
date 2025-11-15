# AI Learning Project

This project will be used to explore and build a new application using AI tools.

## Math Tools

A comprehensive collection of mathematical functions and utilities for common computational tasks.

### Features

#### Number Theory
- `factorial(n)` - Calculate factorial of a non-negative integer
- `fibonacci(n)` - Calculate the nth Fibonacci number
- `is_prime(n)` - Check if a number is prime
- `gcd(a, b)` - Greatest common divisor
- `lcm(a, b)` - Least common multiple

#### Statistics
- `mean(numbers)` - Calculate arithmetic mean
- `median(numbers)` - Calculate median value
- `standard_deviation(numbers)` - Calculate standard deviation

#### Powers and Roots
- `power(base, exponent)` - Calculate base raised to exponent
- `sqrt(n)` - Calculate square root
- `is_perfect_square(n)` - Check if number is a perfect square

#### Geometry
- `distance_2d(x1, y1, x2, y2)` - Calculate Euclidean distance between two 2D points

#### Algebra
- `quadratic_formula(a, b, c)` - Solve quadratic equations (ax² + bx + c = 0)

#### Utilities
- `percentage(part, whole)` - Calculate percentage
- `clamp(value, min_value, max_value)` - Clamp value between min and max

### Usage

```python
from src.math_tools import factorial, is_prime, mean, distance_2d

# Calculate factorial
result = factorial(5)  # Returns 120

# Check if number is prime
is_17_prime = is_prime(17)  # Returns True

# Calculate mean of numbers
average = mean([10, 20, 30, 40, 50])  # Returns 30.0

# Calculate distance between points
dist = distance_2d(0, 0, 3, 4)  # Returns 5.0
```

### Running Examples

To see all functions in action, run the examples script:

```bash
python examples.py
```
