fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:" , fname)
    exit()

count = 0
number = 0
for line in fhand:
    
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        colon_pos = line.find(':')
        number += float(line[colon_pos+1:].strip())

print("Average spam confidence:", number / count)