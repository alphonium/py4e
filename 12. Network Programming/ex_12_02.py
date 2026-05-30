import socket

url = input("Enter the URL: ")
if len(url) < 1:
    url = 'http://data.pr4e.org/romeo.txt'
try:
    host = url.split('/')[2]
except:
    print("Invalid URL", url)
    exit()

print()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())

count = 0
limit = 3000
displayed = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    text = data.decode()
    for ch in text:
        count += 1
        if displayed < limit:
            print(ch, end='')
            displayed += 1 
    
print('\n')
print("Total characters received:", count)
print("Total characters displayed:", count if count <= limit else limit)

mysock.close()
