## This is an archived repository.
I recommend using youtube-dl instead: https://github.com/rg3/youtube-dl
It supports downloading playlists using the command line flag --playlist-start, and many other options.

# youtube-playlist-downloader
A Python CLI utility to download an entire playlist from YouTube.

To run, clone this repository into an empty directory:
 `git clone https://github.com/hmspisharody/youtube-playlist-downloader.git`
 
Then install the one dependency:
 `pip install pytube`
 
Finally run the script:
 `python playlist-downloader.py`
 
Just copy the youtube playlist link to clipboard and call 'python playlist-downloader.py'.
It will create a folder within the folder where the script resides and downloads all the videos into it.
 
The script checks if the videos from the playlist are already in the destination directory.
This means you can re-run the script and only download the newly uploaded content.
