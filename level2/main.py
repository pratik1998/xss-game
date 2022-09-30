from flask import render_template, make_response

def get_home_page():
    return render_template('level2/home.html')

def get_frame_page():
    resp = make_response(render_template('level2/frame.html'))
    resp.headers['Content-Security-Policy'] = ("default-src 'self';" +
        "script-src 'self';" +
        "style-src 'self' http://fonts.googleapis.com 'sha256-NT975AHrbM1rOKWHz7wVzG2s9/CKoxikN97C34fq2do=';"
    )
    return resp

def get_source_page():
    return render_template('level2/source.html')