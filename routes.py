from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Translator')

@app.route('/question')
def question():
    return render_template('question.html', title='Questionairre')

@app.route('/about')
def about():
    return render_template('about.html', title='About')
