# 2. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:

bill = float(input("Total bill amount?"))
service = input("Level of service? ")
split = int(input("Split how many ways? "))
lower_service = service.lower()
tip = 0
if lower_service == 'good':
    tip = bill * .20
elif lower_service == 'fair':
    tip = bill * .15
elif lower_service == 'bad':
    tip = bill * .10
else:
    print('Invalid input')
total_per_person = (tip + bill) / split
print("Tip amount: $%.2f" % (tip))
print("Total amount: $%.2f" % (bill + tip))
print("Amount per person: $%.2f" % total_per_person)

#SOLVED