from flask import render_template, make_response
from utils import generate_nonce_str_from_list, generate_nonces

def get_home_page():
    return render_template('level3/home.html')

def get_frame_page():
    nonces = generate_nonces(3)
    data = {
        'gameFrameNonce': nonces[0],
        'googleAJAXNonce': nonces[1],
        'frameNonce': nonces[2]
    }
    resp = make_response(render_template('level3/frame.html', nonce_data=data))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list(nonces)};'
    return resp

def get_source_page():
    return render_template('level3/source.html')