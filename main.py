from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")
@app.route('/show.html')
def show():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=False, port=80)

