
from flask import Flask, jsonify, render_template, request
import webbrowser
import time

app = Flask(__name__)

@app.route('/_stuff', methods = ['GET'])
def stuff():
    t = time.localtime()
    current_time = time.strftime("%M.%S °C", t)
    return jsonify(result=current_time)


@app.route('/')
def index():
   
    return render_template('dy1.html')

    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)