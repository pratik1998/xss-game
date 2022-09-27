from flask import render_template

def get_home_page():
    return render_template('level6/home.html')

def get_frame_page():
    return render_template('level6/frame.html')

def get_source_page():
    return render_template('level6/source.html')
