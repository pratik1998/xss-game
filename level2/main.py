from flask import render_template

def get_home_page():
    return render_template('level2/home.html')

def get_frame_page():
    return render_template('level2/frame.html')

def get_source_page():
    return render_template('level2/source.html')