from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_curriculo')
def criar_curriculo():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
