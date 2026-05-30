import socket

url = input("Enter the URL: ")
try:
    host = url.split('/')[2]
except:
    print("Invalid URL", url)
    exit()

print()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
print(cmd)
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
