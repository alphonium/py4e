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

max_count = max(list(senders.values()))
for sender, count in senders.items():
    if count == max_count :
        print(sender, count)
