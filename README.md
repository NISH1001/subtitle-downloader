# subtitle-downloader
A simple script to download subtitle from http://thesubdb.com/

-----------

## Dependencies
It requires `python3` and `request`.  
To install `request`, you need `pip3` for python3.

```bash
pip3 install request
```

## Usage
You can directly run the script `subdownloader.py` with the queries supplied from the command line.  
If you make the script executable and add it to the system path, then you can directly run the script.  

Help

```bash
subdownloader.py --help
```

Download subtitles for all the videos in the current directory:

```bash
subdownloader.py --current
```

Download subtitles for all the videos in the specified directory:

```bash
subdownloader.py --dir /home/paradox/test/
```
