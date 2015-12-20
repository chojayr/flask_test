from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/test')

def index():
    return render_template('index.html')


def crt_fle():
    testfile = 'sampl1'
    tes = open(testfile, 'a')
    tes.close()

    return render_template('index.html')


@app.route('/')
def rd_file():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

