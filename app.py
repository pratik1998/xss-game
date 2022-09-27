from math import exp
import os
from flask import Flask, request, make_response, render_template
from level1.main import get_home_page as level1_home_page, get_frame_page as level1_frame_page, get_frame_query_page as level1_frame_query_page, get_source_page as level1_source_page
from level2.main import get_home_page as level2_home_page, get_frame_page as level2_frame_page, get_source_page as level2_source_page
from level3.main import get_home_page as level3_home_page, get_frame_page as level3_frame_page, get_source_page as level3_source_page
from home import get_home_page
from datetime import datetime, timedelta

from flask import send_from_directory

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

def generate_cookie():
    return os.urandom(16).hex()

cookie_store = {}

def store_cookie(level, value):
    if cookie_store.get(level, None) is None:
        cookie_store[level] = list()
    cookie_store[level].append(value)

def validate_cookie(level, value):
    if cookie_store.get(level, None) is None:
        return False
    return value in cookie_store[level]

# Home page routes

@app.route("/")
def index():
    return get_home_page()

@app.route('/favicon.ico', methods=['GET'])
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Level 1 routes

@app.route("/level1", methods=['GET'])
def level1():
    return level1_home_page()

@app.route("/feedback/level1/<path:path>", methods=['GET'])
def level1_feedback(path):
    return 'OK'

@app.route("/level1/frame", methods=['GET'])
def level1_frame():
    query = request.args.get('query')
    if query is not None:
        return level1_frame_query_page(query)
    return level1_frame_page()

@app.route("/level1/source", methods=['GET'])
def level1_source():
    return level1_source_page()

@app.route("/level1/record", methods=['GET'])
def level1_record_feedback():
    resp = make_response('OK')
    cookie_value = generate_cookie()
    resp.set_cookie('level1', cookie_value, httponly=True, expires=datetime.now() + timedelta(days=30))
    store_cookie('level1', cookie_value)
    return resp


# Level 2 routes
@app.route("/level2", methods=['GET'])
def level2():
    # level1_cookie = request.cookies.get('level1')
    # if level1_cookie and validate_cookie('level1', level1_cookie):
    #     return level2_home_page()
    # return render_template('error/error.html')
    return level2_home_page()

@app.route("/level2/<path:path>", methods=['GET'])
def level2_payload_response(path):
    return level2_home_page()

@app.route("/level2/frame", methods=['GET'])
def level2_frame():
    return level2_frame_page()

@app.route("/level2/source", methods=['GET'])
def level2_source():
    return level2_source_page()

@app.route("/feedback/level2/<path:path>", methods=['GET'])
def level2_feedback(path):
    return 'OK'

@app.route("/level2/record", methods=['GET'])
def level2_record_feedback():
    resp = make_response('OK')
    cookie_value = generate_cookie()
    resp.set_cookie('level2', cookie_value, httponly=True, expires=datetime.now() + timedelta(days=30))
    store_cookie('level2', cookie_value)
    return resp

# Level 3 routes
@app.route("/level3", methods=['GET'])
def level3():
    # Skipping cookie validation so we can move between levels
    # level1_cookie = request.cookies.get('level2')
    # if level1_cookie and validate_cookie('level1', level1_cookie):
    #     return level2_home_page()
    # return render_template('error/error.html')
    return level3_home_page()

@app.route("/level3/<path:path>", methods=['GET'])
def level3_payload_response(path):
    return level3_home_page()

@app.route("/level3/frame", methods=['GET'])
def level3_frame():
    return level3_frame_page()

@app.route("/level3/source", methods=['GET'])
def level3_source():
    return level3_source_page()

@app.route("/feedback/level3/<path:path>", methods=['GET'])
def level3_feedback(path):
    return 'OK'

@app.route("/level3/record", methods=['GET'])
def level3_record_feedback():
    resp = make_response('OK')
    cookie_value = generate_cookie()
    resp.set_cookie('level3', cookie_value, httponly=True, expires=datetime.now() + timedelta(days=30))
    store_cookie('level3', cookie_value)
    return resp

# Level 4 routes
