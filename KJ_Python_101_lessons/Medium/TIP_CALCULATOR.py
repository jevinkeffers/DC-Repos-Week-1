#1. TIP CALCULATOR 
# Good -> 20%
# Fair -> 15%
# Bad -> 10%

bill = float(input("Total bill amount? "))
service = input("Level of service? ")
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
total = tip + bill
print("Tip amount: $%.2f" % (tip))
print("Total amount: $%.2f" % (bill + tip))