import re

fhand = open('../data/mbox.txt')
query = input("Enter query: ")
count = 0
for line in fhand:
    line = line.strip()
    x = re.findall(query, line)
    if len(x) > 0:
        count += 1
    
print(count)