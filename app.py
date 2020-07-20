
from flask import Flask, jsonify, render_template, request
import webbrowser
import time
import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)

app = Flask(__name__)

@app.route('/_stuff', methods = ['GET'])
def stuff():
    try:
        if(ser.in_waiting >0):
            line = ser.readline()
            print(line)
            current_time = line + '°C'
    except:
        current_time = '0.00°C'
        
    # t = time.localtime()
    # current_time = time.strftime("%M.%S °C", t)
    return jsonify(result=current_time)


@app.route('/')
def index():
   
    return render_template('dy1.html')

    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)