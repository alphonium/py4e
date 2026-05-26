fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

count = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From" : continue
    count[words[2]] = count.get(words[2], 0) + 1
print(count)