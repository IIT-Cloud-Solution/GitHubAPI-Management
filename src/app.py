from flask import Flask, jsonify, request
import os
import requests
from route_functions import fetch_commit_details

from dotenv import load_dotenv
load_dotenv()


BASE_URL = os.environ.get("BASE_URL")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

headers = {
    'Authorization': f'token {ACCESS_TOKEN}',
    'X-GitHub-Api-Version': '2022-11-28'
}



flask_app1 = Flask(__name__)


@flask_app1.route('/')
def index():
    print(BASE_URL)
    return 'Hello Your App is Working!!!'


@flask_app1.route('/all_commits', methods=['GET', 'POST'])
def get_all_user_commits():
    owner = request.form.get('owner')
    repo = request.form.get('repo')

    if not owner or not repo:
        return jsonify({"error": "Missing owner or repo parameters"}), 400
    
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits" # https://api.github.com/repos/lahiru-98/ESD/commits
    print("BASE URL ---> ", url)
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": "Error fetching data from GitHub"}), response.status_code

    commits_info = response.json()

    res = fetch_commit_details(commits_info)  

    return jsonify(res)


if __name__ == '__main__':
    flask_app1.run(host='0.0.0.0', port=5001)