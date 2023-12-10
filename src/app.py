from flask import Flask, jsonify, request
import os
import requests
from route_functions import fetch_commit_details, filter_json

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
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Error fetching data from GitHub"}), response.status_code

    commits_info = response.json()

    res = fetch_commit_details(commits_info)  

    return jsonify(res)


#Endpoint to get the User information
@flask_app1.route('/user_info', methods=['GET'])
def get_user_info():
    username = request.form.get('username')

    if not username:
        return jsonify({"error": "Missing username parameter"}), 400

    url = f"{BASE_URL}/users/{username}" #https://api.github.com/users/lahiru-98
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": "Error fetching data from GitHub"}), response.status_code

    user_info = response.json()
    filtered_user_info = filter_json(user_info, 
                                     ['id','name', 'created_at','followers', 'following', 'collaborators', 
                                      'owned_private_repos', 'public_repos', 'url', 'private_gists', 'public_gists'])
    return jsonify(filtered_user_info)

@flask_app1.route('/check')
def check():
    owner = request.form.get('owner')
    repo = request.form.get('repo')
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    
    res = f"{url} and {ACCESS_TOKEN}"

    return "--> "+res


if __name__ == '__main__':
    flask_app1.run(host='0.0.0.0', port=8080)