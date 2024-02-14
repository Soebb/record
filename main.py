import os
import requests
from github import Auth, Github
token = os.environ.get("token")
auth = Auth.Token(token)
g = Github(auth=auth)
model_url = "https://huggingface.co/gyroing/Persian-Piper-Model-gyro/resolve/main/fa_IR-gyro-medium.onnx"
data = requests.get(model_url, allow_redirects=True)
with open("faa_model.onnx", 'wb') as file:
    file.write(data.content)
with open('faa_model.onnx', 'rb') as file:
    content = file.read()
repo = g.get_user().get_repo("persian-tts-bot")
# Upload to github
git_prefix = 'fa_model/'
git_file = git_prefix + 'gyro_model.onnx'
repo.create_file(git_file, "committing files", content, branch="main")
