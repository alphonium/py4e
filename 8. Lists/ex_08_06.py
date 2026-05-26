nums = []

while True:
    n = input("Enter a number: ")
    if n == 'done':
        break
    else:
        try:
            n = int(n)
        except:
            print("Invalid input")
            continue
        nums += [n]

maximum = max(nums)
minimum = min(nums)
print("Maximum is", maximum)
print("Minimum is", minimum)