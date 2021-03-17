# ytdl

These instructions will help you attempt to grab the associated audio files attached to a given set of Youtube URLs. 
This is equal to downloading music from the command line! :D 

## Requirements

```
pip3 install youtube-dl 
```

## Usage

```
youtube-dl ytsearch:searchTerm
youtube-dl ytsearch<count>:searchTerm
youtube-dl ytsearchall:searchTerm
```
  
Example:

```
youtube-dl -f bestaudio --extract-audio --audio-format mp3 --add-metadata --no-overwrites ytsearch5:KMFDM 
[youtube:search] query "KMFDM": Downloading page 1
[youtube:search] playlist KMFDM: Downloading 5 videos
[download] Downloading video 1 of 5
[youtube] xwhOTNQcQq4: Downloading webpage
[download] Destination: KMFDM - Megalomaniac-xwhOTNQcQq4.webm
[download] 100% of 5.67MiB in 00:09
[ffmpeg] Destination: KMFDM - Megalomaniac-xwhOTNQcQq4.mp3
Deleting original file KMFDM - Megalomaniac-xwhOTNQcQq4.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'KMFDM - Megalomaniac-xwhOTNQcQq4.mp3'
[download] Downloading video 2 of 5
[youtube] 06nnZydpZJE: Downloading webpage
[download] Destination: KMFDM - Angst (1993) full album-06nnZydpZJE.webm
[download] 100% of 45.40MiB in 01:06
[ffmpeg] Destination: KMFDM - Angst (1993) full album-06nnZydpZJE.mp3
Deleting original file KMFDM - Angst (1993) full album-06nnZydpZJE.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'KMFDM - Angst (1993) full album-06nnZydpZJE.mp3'
[download] Downloading video 3 of 5
[youtube] q832CI2S3b0: Downloading webpage
[download] Destination: KMFDM - Megalomaniac-q832CI2S3b0.webm
[download] 100% of 5.84MiB in 00:07
[ffmpeg] Destination: KMFDM - Megalomaniac-q832CI2S3b0.mp3
Deleting original file KMFDM - Megalomaniac-q832CI2S3b0.webm (pass -k to keep)
etc
```

for more information, check out https://github.com/ytdl-org/youtube-dl/blob/master/README.md#options
