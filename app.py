import os
from flask import Flask, request
from level1.main import get_home_page as level1_home_page, get_frame_page as level1_frame_page, get_frame_query_page as level1_frame_query_page, get_source_page as level1_source_page
from home import get_home_page

from flask import send_from_directory

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

@app.route("/")
def index():
    return get_home_page()

# from flask import send_from_directory

# # @app.route('/static/logos/<path:path>')
# # def send_report(path):
# #     return send_from_directory('static/logos', path)

# @app.route('/static/<path:path>')
# def send_report(path):
#     return send_from_directory('static', path)

@app.route('/favicon.ico', methods=['GET'])
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

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