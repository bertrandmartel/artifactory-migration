# Artifactory Migration script

Python scripts to quickly migrate artifacts from/to artifactory instances

* download all artifacts from a specific repo in artifactory
* upload all artifacts from a specific folder to artifactory

## Download all artifacts for a repo

* set the following env var:

  * ARTIFACTORY_ORIGIN_URL : artifactory base URL ex: https://your.artifactory.host/artifactory
  * ARTIFACTORY_ORIGIN_USERNAME : artifactory username
  * ARTIFACTORY_ORIGIN_PASSWORD : artifactory password

* edit the repo name value and output directory if needed in the script and run :

```bash
python3 download_artifacts.py
```

default repo is `maven-all`

## Upload artifacts to artifactory

* set the following env var:

  * ARTIFACTORY_DEST_URL : artifactory base URL ex: https://your.artifactory.host/artifactory
  * ARTIFACTORY_DEST_USERNAME : artifactory username
  * ARTIFACTORY_DEST_PASSWORD : artifactory password

* edit output directory if needed in the script and run :

```bash
python3 upload_artifacts.py
```

