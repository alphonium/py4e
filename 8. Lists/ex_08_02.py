fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:" , fname)
    exit()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != "From" : continue
    if len(words) < 3 : continue    
    print(words[2])