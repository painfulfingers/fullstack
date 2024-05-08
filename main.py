from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from moviepy.editor import *
import os
import urllib.request
from flask_cors import CORS
from urllib.parse import urlencode
from flask import Flask,redirect,url_for,request,jsonify,session
import requests
import time
import base64

client_id="ffdf2044e54040ca9536e13c3f906f73"
client_secret="545d5a378edb47718d0a2409dbdc7bad"

url = "https://accounts.spotify.com/authorize?"
url_token = "https://accounts.spotify.com/api/token"
url_imf = "https://api.spotify.com/v1/me"
url_playlist = "https://api.spotify.com/v1/users/"
url_me_playlist = "https://api.spotify.com/v1/me/playlists"


url_search = "https://api.spotify.com/v1/search"

scope = "playlist-read-collaborative playlist-read-private user-read-private user-read-email playlist-modify-public playlist-modify-private"
params = {
    "response_type":'code',
    "client_id": client_id,
    "scope": scope,
    "state": "gsvcvzcxzvcxvx",
    "redirect_uri":"http://127.0.0.1:5000/callback"
}

# def url_to_binary(url):
#     with urllib.request.urlopen(url) as response:
#         binary_data = response.read()
#     return binary_data


# Concatenate client ID and client secret with a colon
auth_string = f"{client_id}:{client_secret}"

# Encode the auth string to bytes using ASCII encoding
auth_bytes = auth_string.encode("ascii")

# Base64 encode the bytes
auth_base64 = base64.b64encode(auth_bytes)

# Convert the base64 encoded bytes to a UTF-8 string
auth_base64_str = auth_base64.decode("utf-8")

print(auth_base64_str)

encoded =  base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii") 
    
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "gasioigdsfgeofkaep[fl]"

# def store_binary_data(binary_data, file_path):
#     assert os.path.isfile(file_path)
#     with open(file_path, 'rb') as file:
#         file.write(binary_data)
#     print("Binary data has been successfully stored in:", file_path)


# driver = webdriver.Chrome()
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
# new_link = "https://wwwcom"
# driver.get(new_link)
# driver.find_element(By.TAG_NAME, "a").click()
# price = driver.find_element(By.CLASS_NAME,"a-price-whole")
# print(price.text)
# input = driver.find_element(By.CSS_SELECTOR, "#xv-search-form .search-input")
# input.send_keys("moaning videos", Keys.ENTER)
# driver.find_element(By.CSS_SELECTOR, '#video_14194135 a').click()
# video_content = driver.find_element(By.CSS_SELECTOR, "#hlsplayer video").get_attribute('src')
# file_name = "test.mp4"
# urllib.request.urlretrieve(video_content, file_name)
# cvt_video = VideoFileClip(file_name)
# ext_audio = cvt_video.audio
# ext_audio.write_audiofile("extracted.mp3")
new_dict = {}
@app.route("/")
def hello_world():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    encoded_params = urlencode(params)
    url = f"https://accounts.spotify.com/authorize?{encoded_params}"
    return redirect(url)


@app.route("/success")
def success():
    return "congrats on first step"

@app.route('/callback',methods=['GET', 'POST'])
def callback():
        data = request.data
        new_string = data.decode('utf-8')
        print(new_string)
        params = {
            'code':new_string,
            'redirect_uri': 'http://localhost:4200//callback',
            'grant_type':'authorization_code'
        }
        headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic ' +  auth_base64_str
        }
        token = requests.post(url_token, params=params, headers=headers)
        response =  token.json()
        session["access_token"] = response["access_token"]
        session["expires_in"] = int(time.time()) + 3600
        session["refresh_token"] = response["refresh_token"]
        print(session=["access_token"])
        return redirect(url_for('user_playlist'))


def refresh_token():
    if session["expires_in"] <= time.time():
        params={
            "grant_type":"refresh_token", 
            "refresh_token":session["refresh_token"]
        }
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' +  auth_base64_str
        }
        token = requests.post(url_token,params=params,headers=headers)
        response = token.json()
        session["access_token"] = response["access_token"]
        session["expires_in"] =int(time.time()) + int(response["expires_in"])
        session["refresh_token"] = response["refresh_token"]
    


@app.route('/user_playlist/api/playlist-items/<playlist_id>', methods=['GET'])
def get_playlist_items(playlist_id):
    access_token = new_dict["session"]
    if not access_token:
        return jsonify({'error': 'Access token not found'}), 401
    params={
        'market':'IN'
    } 
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    response = requests.get(url,headers=headers,params=params)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch playlist items'}), response.status_code
    return response.json()
    

@app.route('/play/<song1>/<song2>/<song3>',methods=['GET', 'POST'])
def play_the_list(song1,song2,song3):
    access_token = new_dict["session"]
    headers = {'Authorization': f'Bearer {access_token}',
               'content_type':'application/json'}
    Body = {
        "uris": ["spotify:track:"+song1, "spotify:track:"+song2,"spotify:track:"+song3]
    }
    response = requests.put('https://api.spotify.com/v1/me/player/play',json=Body,headers=headers)
    print(response.json())
    return response.json()

@app.route('/pause',methods = ['GET','POST'])
def pause():
    access_token = new_dict["session"] 
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.put('https://api.spotify.com/v1/me/player/pause',headers=headers)
    return response.json()


@app.route('/user_playlist',methods=['GET', 'POST'])
def user_playlist():
    if request.method == 'POST':  
      data = request.data
      new_string = data.decode('utf-8')
      print(new_string)
      new_dict["session"] = new_string
      headers = {
    'Authorization': 'Bearer ' + new_string
    }    
      dev = requests.get(url_playlist + '9h9x91qa9veat6cx5oa3ii8a3' + "/playlists",  headers=headers)
      new_dict['save1']=dev.json()
    if request.method == 'GET':
        return new_dict['save1']
    # return jsonify([{'add':'taste'}])


@app.route('/create_playlist')
def create_playlist(): 
    if "access_token" not in session:
       redirect(url_for('login'))
    refresh_token()       
    Body = {
         "name": "experiment de groupe",
         "description": "french accent",
         "public": True
    }

    headers = {
    'Authorization': 'Bearer ' + session["access_token"],
    'Content-Type': 'application/json'
    }    

    devi = requests.post(url_playlist + "9h9x91qa9veat6cx5oa3ii8a3" + "/playlists", json=Body, headers=headers)
    return devi.json()


@app.route('/search')
def search(): 
    if "access_token" not in session:
        redirect(url_for('login'))
    refresh_token() 
    headers = {
    'Authorization': 'Bearer ' + session["access_token"]
    }    

    params = {
        "q":'remaster%20track:Doxy%20artist:Miles%20Davis',
        "type": 'album',
        "market": "ES"
    }
    devi = requests.get(url_search,params=params,headers=headers)
    return devi.json() 


if __name__ == '__main__':
    app.run(debug=True)


