import re

fhand = open('../data/mbox.txt')

count = 0
for line in fhand:
    line = line.strip()
    x = re.findall('^Author', line)
    count += 1
    
print(count)