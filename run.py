#!/usr/bin/env python3
import json
import subprocess
import os
import time
from optparse import OptionParser

from flask import Flask, request

app = Flask(__name__)
secret_path = '/lain/app/deploy/secrets.json'


def parse():
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port', type=int, default=5000)
    parser.add_option('-s', '--sleep', dest='sleep', type=int, default=0)
    parser.add_option('-i', '--interval', dest='interval', type=int, default=0)
    options, _ = parser.parse_args()
    return options.port, options.sleep, options.interval


port, sleep, interval = parse()


@app.route('/echo')
def echo():
    msg = 'Request Headers: {}'.format(request.headers)
    return msg


@app.route('/')
def index():
    xff = request.headers.get('X-Forwarded-For', 'no xff set')
    host_ip = subprocess.check_output(['hostname', '-i']).strip()
    try:
        secret = open(secret_path).read()
    except FileNotFoundError:
        secret = ''

    res = {'xff': xff, 'hostname': host_ip, 'env': os.environ, 'secretfile': secret}
    return json.dumps(res)


print('Taking a nap before starting...')
time.sleep(sleep)
print('Waking up...')
app.run('0.0.0.0', port=port)
