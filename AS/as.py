from socket import *
map = {}

ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(('', 53533))

while True:
    msg, address = ss.recvfrom(2048)
    message = msg.decode()
    m = message.split('\n')
    key = m[1].split('=')[1]
    if 'VALUE' in message:
        value = m[2].split('=')[1]
        map[key] = value
        ss.sendto(value.encode(),address)
    else:
        if key in map:
            response = "TYPE=A\nNAME={}\nVALUE={}\nTTL=10".format(key,map[key])
            ss.sendto(response.encode(), address)
