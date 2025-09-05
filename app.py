from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/contacto')
def contacto():
    return render_template('contactanos.html')

@app.route('/politicas')
def politicas():
    return render_template('politicas.html')

if __name__ == '__main__':
    app.run(debug=True)