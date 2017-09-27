from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/github')
def linkd():
    return render_template('github.html')


@app.route('/gplus')
def github():
    return render_template('gplus.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

