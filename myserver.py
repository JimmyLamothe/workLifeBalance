from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/display/<text>')
def display(text):
    templateData = {
        'text' : text
    }
    return render_template('display.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
