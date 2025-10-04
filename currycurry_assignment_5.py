# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")

# Ask the user for a starting number
x = int(input("Enter starting number: "))

# Set up a list to store the sequence and a counter for steps
sequence = []
steps = 0
n = x

# Keep going until n becomes 1
while n != 1:
    sequence.append(n)
    if n % 2 == 0:
        n //= 2  # If even, divide by 2
    else:
        n = 3 * n + 1  # If odd, multiply by 3 and add 1
    steps += 1

# Add the final number 1 to the sequence
sequence.append(1)

# Show the full sequence and number of steps
print("Sequence:", " ".join(map(str, sequence)))
print("Steps:", steps)

# === Challenge 2: Prime Number Checker ===
print("\n=== Challenge 2: Prime Number Checker ===")

# Ask the user for a number
a = int(input("Enter a number: "))

# Show what numbers we’re checking
print(f"Testing divisors from 2 to {a-1}...")

# Assume the number is prime
is_prime = True

# Check if a is divisible by any number up to its square root
for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        print(f"{a} is not prime (divisible by {i})")
        is_prime = False
        break

# If no divisors found, it’s prime
if is_prime:
    print(f"{a} is prime!")

# === Challenge 3: Multiplication Table ===
print("\n=== Challenge 3: Multiplication Table ===")

# Print the top row (1 to 10)
print("     ", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print()

# Print each row of the table
for i in range(1, 11):
    print(f"{i:2}", end=" ")  # Row label
    for j in range(1, 11):
        print(f"{i*j:4}", end="")  # Multiply and print
