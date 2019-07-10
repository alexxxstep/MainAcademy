import math
import random

# Generate sequence 5 integers long from range(0, 100)
x = [random.randint(1, 100) for i in range(5)]

# Generate random float
v_fl = random.random()

# Print variables above
print(x)
print(random.random())

# Find max element from generated sequence
mx = max(x)
print(mx)

# Make a floor division between max element and generated float
d_v = int(mx / v_fl)
print(d_v)

# Find factorial of the result above
fctl = math.factorial(d_v)
print(fctl)



