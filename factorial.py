
import math

# Compute factorials of numbers from 1 to 12
factorials = {num: math.factorial(num) for num in range(1, 13)}

# Print the computed factorials
for num, fact in factorials.items():
    print(f"Factorial of {num} is {fact}")

# Compute squares  of numbers from 1 to 12
squares = {num: num**2 for num in range(1, 13)}


# Print the computed squaresf
for num, square  in squares.items():
    print(f"square of {num} is {square}")
