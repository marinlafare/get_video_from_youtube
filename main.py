from download_videos import get_video
import os

if __name__ == '__main__':
    URL = input('URL please :::  ')
    get_video(URL)
    print('VIDEO READY AT VIDEO FOLDER')