import re

fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = '../data/mbox.txt'
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

query = '^New Revision: ([0-9]+)$'
numbers = list()
for line in fhand:
    line = line.strip()
    results = re.findall(query, line)
    for result in results:
        numbers.append(int(result))   
average = sum(numbers)//len(numbers)
print(average)