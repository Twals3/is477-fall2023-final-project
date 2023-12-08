import requests

wine_url = 'https://archive.ics.uci.edu/static/public/109/wine.zip'

wine_sha256 = "23bd4728d59aa19260aaeec757b4f76eca4baebaf33a94f120086c06e7bc80ef"

wine_dir = './data'

wine_file = './data/wine.zip'

import os

def checkOrMkdir(path: str):
    if (not os.path.exists(path)):
        os.mkdir(path)
        print(f'Created directory: {path}')
    else:
        print(f'{path} detected, skipped mkdir...')

# Create directories if needed
checkOrMkdir('./data')
checkOrMkdir(wine_dir)

# Download adult zip
with open(wine_file, 'wb') as f:
    res = requests.get(wine_url, verify=False)
    assert res.status_code == 200, f"{wine_file} download failed..."
    f.write(res.content)
    f.close()

import hashlib

# Verify adult csv hash value
with open(wine_file, 'rb') as f:
    data = f.read()
    wine_auto_hash = hashlib.sha256(data).hexdigest()
    assert wine_auto_hash == wine_sha256, "Wine zip download failed: sha256 doesn't match"
    print(f"{wine_file} sha256 verified successfully...")

import zipfile

# Extract adult data from zip
with zipfile.ZipFile(wine_file, 'r') as zip_ref:
    zip_ref.extractall(wine_dir)
    zip_ref.close()
    print(f'Extracted files from {wine_file} to {wine_dir}')

# Remove adult zip
os.remove(wine_file)
print(f'Removed {wine_file}')
