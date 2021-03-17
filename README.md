# ytdl

This script will attempt to grab the associated .m4a (or .webm) file attached to a given set of Youtube URLs. 
This is equal to downloading music from the command line! :D 

## Requirements

```
pip3 install youtube-dl 
pip3 install youtube-search-python
```

## Usage

```
python3 ytdl.py "searchTerm" 
python3 ytdl.py "searchTerm" <count>
```
  
Example:

```
python3 ytdl.py "KMFDM" 5
6:08: KMFDM - Megalomaniac Y/N:y
[youtube] xwhOTNQcQq4: Downloading webpage
[download] KMFDM - Megalomaniac-xwhOTNQcQq4.m4a has already been downloaded
[download] 100% of 5.67MiB
[ffmpeg] Correcting container in "KMFDM - Megalomaniac-xwhOTNQcQq4.m4a"
48:44: KMFDM - Angst (1993) full album Y/N:y
[youtube] 06nnZydpZJE: Downloading webpage
[download] KMFDM - Angst (1993) full album-06nnZydpZJE.webm has already been downloaded
[download] 100% of 45.40MiB
6:08: KMFDM - Megalomaniac Y/N:y
[youtube] q832CI2S3b0: Downloading webpage
[download] Destination: KMFDM - Megalomaniac-q832CI2S3b0.webm
[download] 100% of 5.84MiB in 00:00
1:32:38: KMFDM  - Live 30th Anniversary Concert  2013 (2015) Y/N:y
[youtube] pSFRSvbJq0A: Downloading webpage
[download] KMFDM  - Live 30th Anniversary Concert  2013 (2015)-pSFRSvbJq0A.m4a has already been downloaded
[download] 100% of 85.72MiB
[ffmpeg] Correcting container in "KMFDM  - Live 30th Anniversary Concert  2013 (2015)-pSFRSvbJq0A.m4a"
49:00: KMFDM - Nihil  (1995) full album Y/N:y
[youtube] p511mTLz2qU: Downloading webpage
[download] KMFDM - Nihil  (1995) full album-p511mTLz2qU.m4a has already been downloaded
[download] 100% of 44.50MiB
[ffmpeg] Correcting container in "KMFDM - Nihil  (1995) full album-p511mTLz2qU.m4a"
```




