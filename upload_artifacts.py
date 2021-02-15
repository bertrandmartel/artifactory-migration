import requests
from requests.auth import HTTPBasicAuth
import os
import sys
from pathlib import Path

# https://your.artifactory.host/artifactory
baseUrl = os.getenv('ARTIFACTORY_DEST_URL', "")
username = os.getenv('ARTIFACTORY_DEST_USERNAME', "")
password = os.getenv('ARTIFACTORY_DEST_PASSWORD', "")

artifactDir = "artifacts"
repo = "maven-all"

def uploadFile(filename, url):
    try:
        r = requests.put(url,
                         data=open(filename, 'rb').read(),
                         auth=HTTPBasicAuth(username, password))
        print(f"[{r.status_code}] {filename}")
        if r.status_code > 299:
            print(r.text)
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print(
            f'[ERROR] could not upload {url} - {str(err)}')

if username == "" or password == "":
    print("username/password not defined")
    sys.exit()

pathlist = Path(artifactDir).glob('**/*.*')
for filename in pathlist:
    if os.path.isfile(filename):
        splitPath = os.path.split(os.path.abspath(filename))
        path = splitPath[0].split(artifactDir, 1)[1]
        url = f'{baseUrl}{path.replace(os.path.sep, "/")}/{splitPath[1]}'
        print(f"Uploading {url}")
        uploadFile(filename, url)
