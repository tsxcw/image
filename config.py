import json

import util

js = {}


def init():
    global js
    if util.checkFile('./config.json'):
        f = open('./config.json', 'br').read().decode('utf-8')
        try:
            js = json.loads(f)
        except Exception:
            pass


def env(key, default=None):
    global js
    if key in js:
        return js[key]
    return default


init()
