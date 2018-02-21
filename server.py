from PIL import Image
from flask import Flask, request
import json
from waitress import serve
import base64
app = Flask(__name__)
from flask import render_template

cpu = "--"

@app.route("/")
def root():
    # Loads the index.html in templates/
    return render_template('index.html', message="Hola!")

@app.route("/login", methods=['GET', 'POST'])
def login():
    content = request.get_json(silent=True)
    if content:
        return json.dumps({'Status':'OK','token':'random'})
    else:
        return json.dumps({"Status":"ERROR"})

@app.route("/job")
def job():
    return json.dumps({'Status':'OK'})

if __name__ == "__main__":
    serve(app,host='0.0.0.0', port=5000)