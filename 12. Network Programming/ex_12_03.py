import socket
import urllib.request, urllib.parse, urllib.error

url = input("Enter the URL: ")
if len(url) < 1:
    url = 'http://data.pr4e.org/romeo.txt'

try:
    fhand = urllib.request.urlopen(url)
    data = fhand.read().decode()
except Exception as e:
    print(f"Error: {e}")

count = 0
limit = 3000
displayed = 0

for ch in data:
    count += 1
    if displayed < limit:
        print(ch, end='')
        displayed += 1 
    
print('\n')
print("Total characters received:", count)
print("Total characters displayed:", min(count, limit))

