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
