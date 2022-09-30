from flask import render_template, make_response

def get_home_page():
    return render_template('level3/home.html')

def get_frame_page():
    resp = make_response(render_template('level3/frame.html'))
    resp.headers['Content-Security-Policy'] = ("default-src 'self';" +
      "script-src 'self' ajax.googleapis.com;" +
      "style-src 'self';"
    )
    return resp

def get_source_page():
    return render_template('level3/source.html')