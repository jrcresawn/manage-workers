#!/usr/bin/env python

import httplib
import urllib
import json
import sys

def update():
    params = urllib.urlencode({'ready': True})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("acic2012.iplantcollaborative.org")
    conn.request("POST", "/cgi-bin/server.py", params, headers)
    r = conn.getresponse()
    if r.status == 200:
        data = r.read()
        print data
        conn.close()
    else:
        sys.exit(1)

update()
