from flask import render_template, make_response
from utils import generate_nonce, generate_nonces, generate_nonce_str_from_list

def get_home_page():
    return render_template('level5/home.html')

def get_frame_page():
    nonce = generate_nonce()
    resp = make_response(render_template('level5/frame.html', nonce=nonce))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list([nonce])};'
    return resp

def get_source_page():
    return render_template('level5/source.html')

def get_signup_page(signup):
    # ALLOWED_NEXT_URLS = ['confirm']
    # if signup not in ALLOWED_NEXT_URLS:
    #     signup = 'confirm'
    nonce = generate_nonce()
    resp = make_response(render_template('level5/signup.html', next=signup, nonce=nonce))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list([nonce])};'
    return resp

def get_confirmation_page(next):
    nonces = generate_nonces(2)
    data = {
        'gameFrameNonce': nonces[0],
        'confirmNonce': nonces[1]
    }
    resp = make_response(render_template('level5/confirm.html', next=next, nonce_data=data))
    resp.headers['Content-Security-Policy'] = f'script-src {generate_nonce_str_from_list(nonces)};'
    return resp