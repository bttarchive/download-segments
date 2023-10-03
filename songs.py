from __future__ import unicode_literals
import subprocess
import sys

with open('dl.txt', 'r', encoding="utf8") as e:
    offset = 0
    check = [line.rstrip().split('\t') for line in e]
    last_row = str(check[len(check) - 1])
    if 'OPTIONS' in last_row:
        offset = 1
        if 'UP' in last_row:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "setuptools", "wheel"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall",
                                   "https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "ffmpeg-python"])
    else:
        print("No additional options given")

from yt_dlp import YoutubeDL

with open('dl.txt', "r") as f:
    lines = [line.rstrip().split('\t') for line in f]

for i in range(0, len(lines)):
    if len(lines[i]) == 1:
        lines[i].append('Song ' + str(i + 1))

with open('failed.txt', 'w') as g:
    for i in range(0, len(lines) - offset):
        try:
            print('Trying to download video', i + 1, 'out of', len(lines) - offset)
            filename = 'Songs/' + lines[i][1]
            link = lines[i][0]
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': filename + '.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([lines[i][0]])
        except:
            print('Video', i + 1, 'failed to download')
            g.write(str(i + 1))
            g.write(' - ')
            g.write(str(lines[i][0]))
            g.write(' - ')
            g.write(str(lines[i][1]))
            g.write('\n')
