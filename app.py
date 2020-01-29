from flask import Flask, render_template, request, jsonify,url_for

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
