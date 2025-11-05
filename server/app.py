from flask import Flask

app = Flask(__name__)


existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']




@app.route('/')
def index():
    return '<h1>Welcome to Flatiron Cars</h1>'
