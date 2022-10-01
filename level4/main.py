from flask import render_template, make_response
from utils import generate_nonce, generate_nonces, generate_nonce_str_from_list

def get_home_page():
    return render_template('level4/home.html')

def get_frame_page():
    nonce = generate_nonce()
    resp = make_response(render_template('level4/frame.html', nonce=nonce))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list([nonce])};'
    return resp

def get_source_page():
    return render_template('level4/source.html')

def get_frame_timer_page(timer):
    try: 
        timer = int(timer)
    except ValueError:
        timer = 3
    nonces = generate_nonces(2)
    data = {
        'gameFrameNonce': nonces[0],
        'timerNonce': nonces[1]
    }
    resp = make_response(render_template('level4/timer.html', timer=str(timer), nonce_data=data))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list(nonces)};'
    return resp