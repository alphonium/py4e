string = 'X-DSPAM-Confidence: 0.8475'

colon_pos = string.find(':')
number = float(string[colon_pos+1:].strip())

print(number)