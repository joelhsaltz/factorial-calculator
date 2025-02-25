
import math

# Compute factorials of numbers from 1 to 10
factorials = {num: math.factorial(num) for num in range(1, 11)}

# Print the computed factorials
for num, fact in factorials.items():
    print(f"Factorial of {num} is {fact}")
