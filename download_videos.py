from pytube import YouTube
import string

VIDEOS_URL = 'videos'

allowed = ''.join([string.ascii_letters + string.digits + '-()'])
def get_clean_title(title):
    new_title = ''        
    for letter in title:
        if letter == ' ':
            new_title += '_'
        if letter not in allowed:
            pass
        else:
            new_title += letter
    return new_title

def get_video(url):
    video_object = YouTube(url)
    clean_title = get_clean_title(video_object.title)
    stream = video_object.streams.get_highest_resolution()
    stream.download(output_path = VIDEOS_URL,
                   filename = clean_title+'.mp4')