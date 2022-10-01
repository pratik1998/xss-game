from flask import render_template, make_response

def get_home_page():
    return render_template('level4/home.html')

def get_frame_page():
    resp = make_response(render_template('level4/frame.html'))
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self';"
    )
    return resp

def get_source_page():
    return render_template('level4/source.html')

def get_frame_timer_page(timer):
    try: 
        timer = int(timer)
    except ValueError:
        timer = 3
    resp = make_response(render_template('level4/timer.html', timer=str(timer)))
    resp.headers['Content-Security-Policy'] = (
      "default-src 'self';" +
      "script-src 'self';" +
      "style-src 'self';"
    )
    return resp