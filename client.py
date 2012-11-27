#!/usr/bin/env python

import httplib
import json
import sys

def update():
    conn = httplib.HTTPConnection("acic2012.iplantcollaborative.org")
    conn.endheaders(message_body=None)
    conn.send(json.dumps({"ready": True}))
    r = conn.getresponse()
    if r.status == 200:
        data = r.read()
        conn.close()
        d = json.loads(data)
        return d['temp']
    else:
        sys.exit(1)
