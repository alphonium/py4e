fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

letters = dict()
for line in fhand:
    words = line.split()
    for word in words:
        for c in word:
            if c > 'A' and c < 'Z':
                c = c.lower()
            if c < 'a' or c > 'z': continue
            letters[c] = letters.get(c, 0) + 1

order = list()
for letter, count in list(letters.items()):
    order.append((count, letter))
order.sort(reverse=True)
for count, letter in order:         
    print(letter, count)