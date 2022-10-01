import os
from utils import *
from flask import render_template, make_response, escape

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script nonce="{nonce}" src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="/static/logos/level1.png">
      <div>
"""
 
page_footer = """
    </div>
  </body>
</html>
"""
 
main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here...">
  <input id="button" type="submit" value="Search">
</form>
<script nonce="{nonce}" type="text/javascript" src="/static/level1/frame.js"></script>
"""

def get_home_page():
    return render_template('level1/home.html')

def get_frame_page():
    nonces = generate_nonces(2)
    resp = make_response(page_header.format(nonce=nonces[0]) + main_page_markup.format(nonce=nonces[1]) + page_footer)
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list(nonces)};'
    return resp

def get_frame_query_page(query):
    # escaped_query = escape(query)
    escaped_query = query
    nonce = generate_nonce()
    message = f"Sorry, no results were found for <b> {escaped_query} </b>."
    message += " <a href='?'>Try again</a>."
    resp = make_response(page_header.format(nonce=nonce) + message + page_footer)
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list([nonce])};'
    return resp

def get_source_page():
    return render_template('level1/source.html')

def get_test_page():
    return "<p>Hello, World!</p>"