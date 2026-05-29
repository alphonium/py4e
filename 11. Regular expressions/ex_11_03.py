import re

fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = 'regex_sum_42.txt'
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

query = '([0-9]+)'
numbers = list()
for line in fhand:
    line = line.strip()
    results = re.findall(query, line)
    for result in results:
        numbers.append(int(result))
print(sum(numbers))