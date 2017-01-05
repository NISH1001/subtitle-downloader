#!/usr/bin/env python3

import hashlib
import os
import shutil
import requests
from bs4 import BeautifulSoup

TEST_FILE_0 = "Futurama.S06E01.Rebirth.avi"
TEST_FILE_1 = "friends.s03e01.720p.bluray.sujaidr.mkv"

def get_hash(file_path):
    """
    The hash is composed by taking the first and the last 64kb of the video file, 
    putting all together and generating a md5 of the resulting data (128kb).
    """
    read_size = 64 * 1024
    with open(file_path, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()

def download(filename):
    """
    This API: http://thesubdb.com/api/  is used in a nutshell
    """
    splitted = os.path.splitext(filename)
    print(splitted)
    headers = {'User-Agent': 'SubDB/1.0 (paradoxical-sub/1.0; https://github.com/NISH1001/subtitle-downloader)'}
    url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(filename) + "&language=en"
    # streaming is enabled for raw bytes
    #response = requests.get(url, headers=headers, stream=True)
    response = requests.get(url, headers=headers)
    with open(splitted[0] + ".srt", "w") as sub:
        """
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                sub.write(response.raw.data)
        """
        sub.write(response.text)


def main():
    download(TEST_FILE_0)
    pass

if __name__ == "__main__":
    main()

