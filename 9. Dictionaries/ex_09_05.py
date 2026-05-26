fname = input("Enter the file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

domains = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != "From" : continue
    email = words[1]
    for i in range(len(email)):
        if email[i] == "@":
            domain = email[i+1:]
    domains[domain] = domains.get(domain, 0) + 1
print(domains)