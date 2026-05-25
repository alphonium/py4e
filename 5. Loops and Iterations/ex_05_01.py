nums = []
total = 0

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

total = sum(nums)
count = len(nums)
average = total/count
print("Total is", total)
print("Count is", count)
print("Average is", average)