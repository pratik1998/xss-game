# xss-game
Repository contains code to run google xss-game (https://xss-game.appspot.com/) in local environment.

# Overview

To run different part of this repository, I created a total of 4 different branches. The following are the branch names
1. xss-game-initial -> this folder contains code to run Google xss game locally
2. xss-game-patched -> this folder contains code to run Google xss game but vulnerabilities are patched in it
3. xss-game-csp-2.0 -> this folder contains code to run Google xss game with added defense using CSP 2.0
4. xss-game-csp-3.0 -> this folder contains code to run Google xss game with added defense using CSP 3.0

# How to Run

To start the web server you need to follow instructions as described below:
1. Clone the repository by running `git clone git@github.com:pratik1998/xss-game.git`
2. Open your terminal and move to the xss-game-initial directory or directory of choosing.
3. Run `python3 -m venv venv`, `source venv/bin/activate` and `pip install -r requirements.txt` commands.
4. Start web server by running `flask --app app run`.
5. Visit the http://localhost:5000 in web browser
6. To move  between different levels try to manually change the suffix of the URL to your level. For example, if you want to visit level1 then go to http://localhost:5000/level1 URL in the web browser.
