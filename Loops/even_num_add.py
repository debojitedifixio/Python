# Write your code below this row 👇

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print(f"Total of even numbers from 1 to 100 is :{total}")
