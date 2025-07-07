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
