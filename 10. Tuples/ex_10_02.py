fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

hours = dict()
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != "From" : continue
    hour = words[5].split(':')[0]
    hours[hour] = hours.get(hour, 0) + 1

for hour, count in sorted(list(hours.items())):
    print(hour, count)