#!/usr/bin/env python3
import json
import os
import time
from optparse import OptionParser

from flask import Flask, request

app = Flask(__name__)
secret_path = '/lain/app/deploy/topsecret.txt'


def parse():
    parser = OptionParser()
    parser.add_option('-p', '--port', dest='port', type=int, default=5000)
    parser.add_option('-s', '--sleep', dest='sleep', type=int, default=0)
    parser.add_option('-i', '--interval', dest='interval', type=int, default=0)
    options, _ = parser.parse_args()
    return options.port, options.sleep, options.interval


port, sleep, interval = parse()


@app.route('/')
def index():
    try:
        secret = open(secret_path).read()
    except FileNotFoundError:
        secret = ''

    hosts = open('/etc/hosts').read()
    res = {
        'env': dict(os.environ),
        'secretfile': secret,
        'hosts': hosts,
    }
    return json.dumps(res)


print('Taking a nap before starting...')
time.sleep(sleep)
print('Waking up...')
app.run('0.0.0.0', port=port)
