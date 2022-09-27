import os
from flask import render_template

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
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""

def get_home_page():
    return render_template('level1/home.html')

def get_frame_page():
    return page_header + main_page_markup + page_footer

def get_frame_query_page(query):
    message = "Sorry, no results were found for <b>" + query + "</b>."
    message += " <a href='?'>Try again</a>."
    return page_header + message + page_footer

def get_source_page():
    return render_template('level1/source.html')

def get_test_page():
    return "<p>Hello, World!</p>"