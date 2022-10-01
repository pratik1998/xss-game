import os
from flask import render_template, make_response, escape

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="/static/game-frame.js"></script>
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
<script type="text/javascript" src="/static/level1/frame.js"></script>
"""

def get_home_page():
    return render_template('level1/home.html')

def get_frame_page():
    resp = make_response(page_header + main_page_markup + page_footer)
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self' http://fonts.googleapis.com;"
    )
    return resp

def get_frame_query_page(query):
    escaped_query = escape(query)
    message = f"Sorry, no results were found for <b> {escaped_query} </b>."
    message += " <a href='?'>Try again</a>."
    resp = make_response(page_header + message + page_footer)
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self' http://fonts.googleapis.com;"
    )
    return resp

def get_source_page():
    return render_template('level1/source.html')

def get_test_page():
    return "<p>Hello, World!</p>"