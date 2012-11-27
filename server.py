#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print

print """
<html>
<head><title></title></head>
<body>
"""

form = cgi.FieldStorage()
ready = form.getvalue("ready", "(no status)")

print """
  <p>Previous message: %s</p>

  <p>form

  <form method="post" action="server.py">
    <p>ready: <input type="text" name="ready"/></p>
  </form>

</body>

</html>
""" % cgi.escape(ready)
