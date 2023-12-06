from flask import Flask, jsonify, request
import os

from dotenv import load_dotenv
load_dotenv()


BASE_URL = os.environ.get("BASE_URL")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")


flask_app1 = Flask(__name__)


@flask_app1.route('/')
def index():
    print(BASE_URL)
    return 'Hello Your App is Working!!!'


if __name__ == '__main__':
    flask_app1.run(host='0.0.0.0', port=5001)