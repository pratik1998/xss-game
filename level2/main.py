from flask import render_template, make_response
from utils import *

def get_home_page():
    return render_template('level2/home.html')

def get_frame_page():
    nonces = generate_nonces(3)
    data = {
        'gameFrameNonce': nonces[0],
        'postStoreNonce': nonces[1],
        'frameNonce': nonces[2]
    }
    resp = make_response(render_template('level2/frame.html', nonce_data=data))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list(nonces)};'
    return resp

def get_source_page():
    return render_template('level2/source.html')