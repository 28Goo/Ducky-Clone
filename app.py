import flask
from flask_session import Session
from tempfile import mkdtemp
import sys
import logging

app = flask.Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    return flask.render_template("landing.html")


@app.route('/zodiac')
def zodiac():
    return flask.render_template('zodiac.html')


@app.route('/one2')
def one2():
    return flask.render_template('one2.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/contact')
def buy():
    return flask.render_template('contact.html')


@app.route('/rat')
def rat():
    return flask.render_template('rat.html')


@app.route('/pig')
def pig():
    return flask.render_template('pig.html')


@app.route('/dog')
def dog():
    return flask.render_template('dog.html')


@app.route('/rooster')
def rooster():
    return flask.render_template('rooster.html')


@app.route('/monkey')
def monkey():
    return flask.render_template('monkey.html')


@app.route('/goat')
def goat():
    return flask.render_template('goat.html')


@app.route('/rosa')
def rosa():
    return flask.render_template('rosa.html')


@app.route('/tuxedo')
def tuxedo():
    return flask.render_template('tuxedo.html')


@app.route('/bon')
def bon():
    return flask.render_template('bon.html')


@app.route('/horizon')
def horizon():
    return flask.render_template('horizon.html')


@app.route('/skyline')
def skyline():
    return flask.render_template('skyline.html')


@app.route('/midnight')
def midnight():
    return flask.render_template('midnight.html')
