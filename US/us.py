from flask import Flask, app, request, Response 
import requests
from socket import *

app = Flask(__name__)

@app.route('/fibonacci', methods = ['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = (request.args.get('as_port'))

    if hostname and fs_port and number and as_ip and as_port:
        cs = socket(AF_INET, SOCK_DGRAM)
        message = "TYPE=A\nNAME={}".format(hostname)
        cs.sendto(message.encode(), (as_ip, int(as_port)))
        msg = cs.recvfrom(2048)
        cs.close()
        msg = msg.decode()
        ipAddr = msg.split('\n')
        ip = ipAddr[2].split('=')[1]
        r = requests.get('http://{}:{}/fibonacci?number={}'.format(ip,fs_port,number))
        return Response(r.text,status=200)
    else:
        return Response("It is a bad request", status=400)



app.run(host = '0.0.0.0',
        port = 8080,
        debug=True)