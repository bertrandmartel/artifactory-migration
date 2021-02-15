import requests
from requests.auth import HTTPBasicAuth
import os
import sys

# https://your.artifactory.host/artifactory
baseUrl = os.getenv('ARTIFACTORY_ORIGIN_URL', "")
username = os.getenv('ARTIFACTORY_ORIGIN_USERNAME', "")
password = os.getenv('ARTIFACTORY_ORIGIN_PASSWORD', "")

artifactDir = "artifacts"
repo = "maven-all"


def createDirectory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def downloadFile(url, dest):
    try:
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        with open(dest, 'wb') as f:
            f.write(r.content)
        return True
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print(
            f'[ERROR] could not download {url} - {str(err)}')
        return False


if username == "" or password == "":
    print("username/password not defined")
    sys.exit()

r = requests.post(f"{baseUrl}/api/search/aql",
                  data='items.find({"repo":"' + repo + '"})',
                  headers={"Content-Type": "text/plain"},
                  auth=HTTPBasicAuth(username, password))

results = r.json()["results"]
createDirectory(artifactDir)
for item in results:
    url = f'{baseUrl}/{item["repo"]}/{item["path"]}/{item["name"]}'
    createDirectory(os.path.join(artifactDir, item["repo"], item["path"]))
    print(f"GET {url}")
    downloadFile(url, os.path.join(
        artifactDir, item["repo"], item["path"], item["name"]))
