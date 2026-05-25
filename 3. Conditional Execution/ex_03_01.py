hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
ot_hrs = hrs - 40
ot_rate = rate * 1.5
if hrs > 40:
    result = 40 * rate + ot_hrs * ot_rate
else:    
    result = hrs * rate
print("Pay:", result)