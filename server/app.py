#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')  # this decorator is an instance method that modifies app
def index():    # creating a rule that requests for the base url should show index- a page
    return '<h1>Welcome to my page!</h1>' # with headers that says "Welcome to my page!"


@app.route('/<string:username>') # Anything included in the route passed to the app.route decorator with angle brackets <> surrounding it will be passed to the decorated function as a parameter
def user(username):               # creating flexible dynamic applications. Validating username as string by specifying it the route.
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)



