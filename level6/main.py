from flask import render_template, make_response
from utils import generate_nonces, generate_nonce_str_from_list

def get_home_page():
    return render_template('level6/home.html')

def get_frame_page():
    nonces = generate_nonces(2)
    data = {
        'gameFrameNonce': nonces[0],
        'frameNonce': nonces[1]
    }
    resp = make_response(render_template('level6/frame.html', next=next, nonce_data=data))
    resp.headers['Content-Security-Policy'] = f"script-src 'self' {generate_nonce_str_from_list(nonces)};"
    return resp

def get_source_page():
    return render_template('level6/source.html')
