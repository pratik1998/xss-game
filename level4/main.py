from flask import render_template

def get_home_page():
    return render_template('level4/home.html')

def get_frame_page():
    return render_template('level4/frame.html')

def get_source_page():
    return render_template('level4/source.html')

def get_frame_timer_page(timer):
    return render_template('level4/timer.html', timer=timer)