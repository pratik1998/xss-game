from flask import render_template, make_response

def get_home_page():
    return render_template('level5/home.html')

def get_frame_page():
    resp = make_response(render_template('level5/frame.html'))
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self';"
    )
    return resp

def get_source_page():
    return render_template('level5/source.html')

def get_signup_page(signup):
    ALLOWED_NEXT_URLS = ['confirm']
    if signup not in ALLOWED_NEXT_URLS:
        signup = 'confirm'
    resp = make_response(render_template('level5/signup.html', next=signup))
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self';"
    )
    return resp

def get_confirmation_page(next):
    resp = make_response(render_template('level5/confirm.html', next=next))
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self';"
    )
    return resp