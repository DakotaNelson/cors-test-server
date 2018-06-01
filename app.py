import random
import string

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return 'Try <a href="/star">/star</a> and <a href="/reflected">/reflected</a>, which return CORS headers "Access-Control-Allow-Origin" of "*" and "whatever you put in the origin header", respectively. Each endpoint also has a version called <a href="/star-with-creds">/star-with-creds</a> or <a href="/reflected-with-creds">/reflected-with-creds</a>, which sends the same CORS headers with the addition of a "Access-Control-Allow-Credentials: true" header.'

@app.route('/none', methods=['GET', 'OPTIONS', 'POST'])
def none():
    token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])

    cookie = request.headers.get("Cookie")
    response = jsonify({'cookies': cookie})

    response.headers.add('X-Access-Token', token)
    response.set_cookie('secret-cookie', token)
    return response

@app.route('/none-with-creds', methods=['GET', 'OPTIONS', 'POST'])
def none_creds():
    token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])

    cookie = request.headers.get("Cookie")
    response = jsonify({'cookies': cookie})
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Max-Age', '0')

    response.headers.add('X-Access-Token', token)
    response.set_cookie('secret-cookie', token)
    return response

@app.route('/star', methods=['GET', 'OPTIONS', 'POST'])
def star():
    token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])

    cookie = request.headers.get("Cookie")
    response = jsonify({'cookies': cookie})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Max-Age', '0')

    response.headers.add('X-Access-Token', token)
    response.set_cookie('secret-cookie', token)
    return response

@app.route('/star-with-creds', methods=['GET', 'OPTIONS', 'POST'])
def star_creds():
    token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])

    cookie = request.headers.get("Cookie")
    response = jsonify({'cookies': cookie})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Max-Age', '0')
    response.headers.add('Access-Control-Allow-Credentials', 'true')

    response.headers.add('X-Access-Token', token)
    response.set_cookie('secret-cookie', token)
    return response

@app.route('/reflected', methods=['GET', 'OPTIONS', 'POST'])
def reflected():
    origin = request.headers.get('origin')
    token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])

    cookie = request.headers.get("Cookie")
    response = jsonify({'cookies': cookie})
    response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Max-Age', '0')

    response.headers.add('X-Access-Token', token)
    response.set_cookie('secret-cookie', token)
    return response

@app.route('/reflected-with-creds', methods=['GET', 'OPTIONS', 'POST'])
def reflected_creds():
    origin = request.headers.get('origin')
    token = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])

    cookie = request.headers.get("Cookie")
    response = jsonify({'cookies': cookie})
    response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Max-Age', '0')
    #$response.headers.add('Access-Control-Expose-Headers', 'X-Access-Token')

    response.headers.add('X-Access-Token', token)
    response.set_cookie('secret-cookie', token)
    return response
