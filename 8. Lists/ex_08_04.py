fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:" , fname)
    exit()

unique = list()
for line in fhand:
    words = line.split()
    if len(words) == 0 : continue
    for word in words:
        if word not in unique :
            unique.append(word)
unique.sort()
print(unique)