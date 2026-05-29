import re

print( sum( [ int(r) for r in re.findall('[0-9]+',open('regex_sum_2377489.txt').read()) ] ) )