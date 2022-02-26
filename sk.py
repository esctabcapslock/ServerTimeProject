import socket

#create an INET, STREAMing socket (IPv4, TCP/IP)

def myrequest (domain):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')

    ROBOT_IP= socket.gethostbyname(domain)
    ROBOT_PORT = 80

    # print(f'domain: {domain}, ip:{ROBOT_IP}')

    client.connect((ROBOT_IP,ROBOT_PORT))


    # print('Socket Connected to ' + ROBOT_IP )

    cmd = f'''GET / HTTP/1.1\r
Host: {domain}\r
User-Agent: [User-Agent]\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate, br\r
DNT: 1\r
Connection: keep-alive\r
\r
'''

    client.send(bytes(cmd+'\0','ascii'))
    #Read the response sent by robot upon connecting
    msg = client.recv(1024).decode('ascii')
    tmp = msg.split('\r\n')
    # print(msg)
    header = dict(map(lambda d:tuple(d.split(':',1)), filter(lambda x:':' in x, tmp)))
    # print(header)
    client.close()
    return header
