from flask import render_template

def get_home_page():
    return render_template('level5/home.html')

def get_frame_page():
    return render_template('level5/frame.html')

def get_source_page():
    return render_template('level5/source.html')

def get_signup_page(signup):
    return render_template('level5/signup.html', next=signup)

def get_confirmation_page(next):
    return render_template('level5/confirm.html', next=next)