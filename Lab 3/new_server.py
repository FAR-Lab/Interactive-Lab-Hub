from flask import Flask
from time import strftime, sleep
test = strftime("%m/%d/%Y %H:%M:%S")

app = Flask(__name__)

@app.route('/')
def index():
    return strftime("%m/%d/%Y %H:%M:%S")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
