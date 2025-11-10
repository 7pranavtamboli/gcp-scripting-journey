# -----------------------------
# Day 5 – Python Logic Practice
# 1. Extended FizzBuzz variant with custom labels (Twiz, Thriz, Fizz)
# 2. Extended FizzBuzz avoiding many elif
# 3. List comprehension and filtering practice
# -----------------------------

# Exercise 1: FizzBuzz
print("Exercise 1: FizzBuzz\n")

for i in range(1, 31):
    if i % 30 == 0:
        print(i,"> TwizThrizFizz")
    elif i % 15 == 0:
        print(i,"> ThrizFizz")
    elif i % 10 == 0:
        print(i,"> TwizFizz")
    elif i % 6 == 0:
        print(i,"> TwizThriz")
    elif i % 2 == 0:
        print(i, "> Twiz")    
    elif i % 3 == 0:
        print(i, "> Thriz")
    elif i % 5 == 0:
        print(i, "> Fizz")
    else:
        print(i)


print("\nExercise 1: Dynamic TwizThrizFizz avoiding many elif\n")

for i in range(1, 31):
    label = ""
    if i % 2 == 0:
        label += "Twiz"
    if i % 3 == 0:
        label += "Thriz"
    if i % 5 == 0:
        label += "Fizz"

    print(f"{i} > {label or i}")

# --------------------------------
# Exercise 2: List Filtering
# --------------------------------
print("\nExercise 2: List Comprehension + Filtering\n")

nums = [2, 7, 11, 15, 17, 18, 20, 26, 27, 33, 40, 41, 50]
even = [n for n in nums if n % 2 == 0]
squares = [n**2 for n in even]

odd = [n for n in nums if n % 2 != 0]

print("Even numbers:", even)
print("Their squares:", squares)

print("\nOdd numbers:", odd)

print(f"\nTotal numbers: {len(nums)}")

print(f"\nEven count: {len(even)}, Odd count: {len(odd)}")
print(f"Max even number: {max(even)}")
print(f"Min odd number: {min(odd)}")
print(f"Sum of even squares: {sum(squares)}")
