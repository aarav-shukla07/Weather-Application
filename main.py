from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('quantum-stackerz.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)