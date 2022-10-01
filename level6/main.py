from flask import render_template, make_response

def get_home_page():
    return render_template('level6/home.html')

def get_frame_page():
    resp = make_response(render_template('level6/frame.html', next=next))
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self';"
    )
    return resp

def get_source_page():
    return render_template('level6/source.html')
