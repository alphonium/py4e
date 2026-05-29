import re

fhand = open('../data/mbox.txt')

count = 0
for line in fhand:
    line = line.strip()
    x = re.findall('^Author', line)
    if len(x) > 0:
        count += 1
    
print(count)