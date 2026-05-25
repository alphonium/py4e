try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    result = hrs * rate
    print("Pay:", result)
except:
    print("Error, please enter numeric input")

