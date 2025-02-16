import tarfile
import zipfile
import requests
import os

INPUT_FILE_PATH = "data/MillionSongSubset"
RESOURCES = [
    "http://millionsongdataset.com/sites/default/files/tasteprofile/sid_mismatches.txt",
    "http://labrosa.ee.columbia.edu/~dpwe/tmp/train_triplets.txt.zip",
    "http://labrosa.ee.columbia.edu/~dpwe/tmp/millionsongsubset.tar.gz",
    "http://millionsongdataset.com/sites/default/files/AdditionalFiles/TRAXLZU12903D05F94.h5",
]

files_downloaded = 0

for resource in RESOURCES:
    # Download all resources
    local_filename = resource[resource.rindex("/") + 1 :]

    try:
        with requests.get(resource, stream=True) as r:
            r.raise_for_status()

            with open(f"data/{local_filename}", "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        files_downloaded += 1
    except Exception as e:
        print(f"Failed to download resource - {resource}.\nError: {e}\nDO NOT PROCEED!")
        break

print(f"{files_downloaded} of {len(RESOURCES)} resources(s) downloaded")

if files_downloaded == len(RESOURCES):
    # Extract compressed resources
    with tarfile.open("data/millionsongsubset.tar.gz", "r:gz") as tar:
        tar.extractall("data/")

    with zipfile.ZipFile("data/train_triplets.txt.zip", "r") as zip:
        zip.extractall("data/")

    # Delete the zip files
    os.remove("data/millionsongsubset.tar.gz")
    os.remove("data/train_triplets.txt.zip")

    print("Done. All data uncompressed successfully.")
