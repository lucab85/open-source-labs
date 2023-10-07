# mortgage_1.9.py

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid += payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid += payment

print("Total paid:", total_paid)
print("Number of months:", months)
