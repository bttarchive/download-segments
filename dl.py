from __future__ import unicode_literals
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "yt_dlp"])

from yt_dlp import YoutubeDL
from yt_dlp.utils import download_range_func


with open('dl.txt', 'r') as f:
    lines = [line.rstrip().split('\t') for line in f]

for i in range(0, len(lines)):
    if len(lines[i]) == 1:
        lines[i].append('Clip ' + str(i + 1))

substring1 = "youtu"
substring2 = "t="

with open('failed.txt', 'w') as g:
    for i in range(0, len(lines)):
        try:
            print('Trying to download video', i + 1, 'out of', len(lines))
            filename = 'Videos/' + lines[i][1]
            link = lines[i][0]

            try:
                if (substring1 in link) and (substring2 in link):
                    timestamp = link.split("t=", 1)[1]
                    if timestamp[-1:] == 's':
                        timestamp = timestamp[:-1]
                    start_second = int(timestamp) - 5
                    end_second = int(timestamp) + 85
                    ydl_opts = {
                        'format': '(bv*[fps>30][height>720]/bv*[fps>30][height<=720]/bv*[height>720]/bv*/best)[ext=mp4] / ' +
                                  'bv*[fps>30][height>720]/bv*[fps>30][height<=720]/bv*[height>720]/bv*/best',
                        'outtmpl': filename + '.%(ext)s',
                        'downloader': 'ffmpeg',
                        'download_ranges': download_range_func(None, [(start_second, end_second)]),
                    }
                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download([lines[i][0]])
                else:
                    ydl_opts = {
                        'format': '(bv*[fps>30][height>720]/bv*[fps>30][height<=720]/bv*[height>720]/bv*/best)[ext=mp4] / ' +
                                  'bv*[fps>30][height>720]/bv*[fps>30][height<=720]/bv*[height>720]/bv*/best',
                        'outtmpl': filename + '.%(ext)s',
                    }
                    with YoutubeDL(ydl_opts) as ydl:
                        ydl.download([lines[i][0]])

            except:
                ydl_opts = {
                    'format': '(bv*[fps>30][height>720]/bv*[fps>30][height<=720]/bv*[height>720]/bv*/best)[ext=mp4] / ' +
                              'bv*[fps>30][height>720]/bv*[fps>30][height<=720]/bv*[height>720]/bv*/best',
                    'outtmpl': filename + '.%(ext)s',
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
