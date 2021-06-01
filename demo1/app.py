from flask import Flask
import userdata

app = Flask(__name__)
userdata.init_app(app)

@app.route('/')
def index():
    return 'foo'
