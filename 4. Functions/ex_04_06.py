def computepay(hours, rate):
    ot_hrs = hrs - 40
    ot_rate = rate * 1.5
    if hrs > 40:
        result = 40 * rate + ot_hrs * ot_rate
    else:    
        result = hrs * rate
    return result

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))   
except:
    print("Error, please enter numeric input")
    quit()


print("Pay:", computepay(hrs, rate))
