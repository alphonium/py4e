import re

fhand = open('../data/mbox.txt')
query = input("Enter a regular expression: ")
count = 0
for line in fhand:
    line = line.strip()
    if re.findall(query, line):
        count += 1
    
print('mbox.txt had', count, 'lines that matched', query)