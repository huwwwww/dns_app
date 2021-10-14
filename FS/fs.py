from flask import Flask, request, Response
from socket import *



app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')
    cs = socket(AF_INET, SOCK_DGRAM)
    message = "TYPE=A\nNAME={}\nVALUE={}\nTTL=10".format(hostname,ip)
    cs.sendto(message.encode(), (as_ip, int(as_port)))
    cs.close()
    return Response("Success", status=201)


def calculate(num):
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    else:
        return calculate(num-1) + calculate(num-2)


@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    if not isinstance(number,int):
        return Response("Bad format", status=400)
    res = calculate(number)
    return Response(str(res), status=200)


app.run(host='0.0.0.0',
        port=9090,
        debug=True)

