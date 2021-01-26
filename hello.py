#!/usr/bin/env python3

import os
import json
import requests
import cgi, cgitb
import secret
import templates
from http.cookies import SimpleCookie

# print('Content-Type: application/octet-stream')
# print(json.dumps(dict(os.environ), indent=2))

# print('Content-Type: application/json')
# print()


# Part 5
# Line 20 to 22 are obtained from Zoe Riell, January 25, 2021
form = cgi.FieldStorage()
user = form.getfirst("username")
pwd = form.getfirst("password")

print('Content-Type: text/html')
if (user == secret.username and pwd == secret.password):
    print("Set-Cookie: UserID={}".format(user))
    print("Set-Cookie: UserPassword={}".format(pwd))

print()

# Part 7
# Line 33 to 39 are obtained from Zoe Riell, January 25, 2021
c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = ""
c_password = ""
if c.get("UserID"):
    c_username = c.get("UserID").value
if c.get("UserPassword"):
    c_password = c.get("UserPassword").value

if not (c_username == secret.username and c_password == secret.password) and not (user == secret.username and pwd == secret.password):
    print("""
    <!doctype html>
    <html>
    <body>
    <h1> HELLO </h1>
    """)
    # Part 2
    # print("<p> QUERY_STRING={} </p>".format(os.environ['QUERY_STRING']))
    # for param in os.environ['QUERY_STRING'].split('&'):
    #     (name, value) = param.split('=')
    #     print("<li><em>{0}</em> = {1}</li>".format(name, value))

    # Part 3
    # print("<p> Browser={} </p>".format(os.environ['HTTP_USER_AGENT']))

    # Part 4
    print("""
        <form method="POST" action="hello.py">
            <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
            <label> <span>Password:</span> <input type="password" name="password"></label>

            <button type="submit"> Login! </button>
        </form>
    """)

    print("<h1>Username: {}</h1>".format(user))
    print("<h1>Password: {}</h1>".format(pwd))

    print("""
    <ul>
    </ul>
    </body>
    </html>
    """)
# Part 6
else:
    if (c_username):
        page = templates.secret_page(c_username, c_password)
    else:
        page = templates.secret_page(user, pwd)
    print(page)