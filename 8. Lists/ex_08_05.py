fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    exit()

count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != "From" : continue
    print(words[1])
    count += 1
print(count)