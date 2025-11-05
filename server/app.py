from flask import Flask

app = Flask(__name__)


existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']




@app.route('/')
def index():
    return '<h1>Welcome to Flatiron Cars</h1>'



@app.route('/models/<model>')
def get_model(model):
    if model in existing_models:
        return f'<h1>"Flatiron {model} is in our fleet"</h1>'
    else:
        return f'<h1>"No models called {model} exists in our catelog"</h1>', 404
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)