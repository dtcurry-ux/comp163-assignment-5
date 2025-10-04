# Python Challenges Assignment

This assignment includes three programming challenges written in Python: Collatz Conjecture, Prime Number Checker, and Multiplication Table. Below is an explanation of the loop choices, how each solution works, and the AI assistance used.

---

## Challenge 1: Collatz Conjecture

### Loop Type Used: `while` loop

### Reason for Choice:
A `while` loop is ideal here because we don't know how many steps it will take for the number to reach 1. The loop continues until the condition `n != 1` is no longer true.

### How It Works:
- The user inputs a starting number.
- The program repeatedly applies the Collatz rules:
  - If the number is even, divide it by 2.
  - If the number is odd, multiply by 3 and add 1.
- Each number is added to a list to form the sequence.
- The loop stops when the number becomes 1.
- The sequence and number of steps are printed.

---

## Challenge 2: Prime Number Checker

### Loop Type Used: `for` loop

### Reason for Choice:
A `for` loop is used to check divisibility from 2 up to the square root of the input number. This is a known optimization for prime checking and the range is predetermined.

### How It Works:
- The user inputs a number.
- The program checks if the number is divisible by any number from 2 to √n.
- If a divisor is found, the number is not prime.
- If no divisors are found, the number is prime.

---

## Challenge 3: Multiplication Table

### Loop Type Used: Nested `for` loops

### Reason for Choice:
Nested `for` loops are used because we need to iterate over rows and columns in a fixed 10x10 grid.

### How It Works:
- The outer loop iterates through numbers 1 to 10 (rows).
- The inner loop iterates through numbers 1 to 10 (columns).
- Each product is printed in a formatted table.

---

## AI Assistance

This assignment was completed with the help of Microsoft Copilot:
- Copilot assisted in commenting on the Python code.
- It helped simplify comments for better readability.
- It provided explanations for loop choices and logic structure.
