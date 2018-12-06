from flask import render_template
from flask import Flask

app = Flask(__name__)

# Load config variables (notably PLAGCOMPS_LOC)
app.config.from_object('config')


@app.route('/index/')
@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/view_doc/')
def a_page():
    return render_template('view_doc.html')
