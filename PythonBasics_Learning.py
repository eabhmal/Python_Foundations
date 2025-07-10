import sys
from pprint import pprint
high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")


for number in range(3):
    print("Attempt", number+1)


for number in range(1, 4):
    print("Attempt", number)

for number in range(1, 4, 2):
    print("Attempt", number)

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count = count + 1
        print(x)
print(f"We have {count} even numbers")


def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


greet("Abhishek", "Malik")


def increment(number, by):
    return number + by


print(increment(2, 1))
message = increment(2, 1)
print(message)


def multiply(x, y):
    return x*y


multiply(2, 3)


def multiply_n(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply_n(2, 3, 4, 5))


def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)


def fizz_buzz(input):
    if (input % 3) == 0 and (input % 5 == 0):
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


print(fizz_buzz(15))

point = (1, 2, 3)
print(point)
print(point[0:2])


values = []
for x in range(5):
    values.append(x*2)
print(values)


sentence = "This is a common interview question"

char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

char_freq_sorted = sorted(
    char_freq.items(),
    key=lambda value: value[1],
    reverse=True)

print(char_freq_sorted[0])


print(sys.path)
