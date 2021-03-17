from youtubesearchpython import VideosSearch
import youtube_dl
from youtube_dl import YoutubeDL
from sys import argv, exit

yo = {'format':'bestaudio/best'}
ydl = YoutubeDL(yo)

# Download
def dl(u):
    global ydl
    ydl.download([u])

def print_usage(argv):
    print(f"Usage: python3 {argv[0]} <searchTerm>")
    print(f"Usage: python3 {argv[0]} <searchTerm> <count>")
    exit(-1)

def check_args(argv):
    if len(argv) != 2 and len(argv) != 3:
        print_usage(argv)

def main():
    check_args(argv)
    searchTerm = argv[1]
    count = 5
    if len(argv) == 3:
        count = int(argv[2])
    videosSearch = VideosSearch(searchTerm, limit=count)
    v_dict = videosSearch.result()
    for key in v_dict:
        result = v_dict[key]
        for subdict in result:
            title = subdict['title']
            duration = subdict['duration']
            link = subdict['link']
            print(f"{duration}: {title} ", end="")
            answer = ""
            while answer.lower() != "y" and answer.lower() != "n":
                answer = input("Y/N:")
            if answer.lower()=="y":
                dl(link)

if __name__ == '__main__':
    main()

