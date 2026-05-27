fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

senders = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != "From" : continue
    senders[words[1]] = senders.get(words[1], 0) + 1

lst = list()
for sender, count in list(senders.items()):
    lst.append((count, sender))

lst.sort(reverse=True)

for count, sender in lst[0:1]:
    print(sender, count)