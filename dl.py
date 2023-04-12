from __future__ import unicode_literals
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "yt_dlp"])

from yt_dlp import YoutubeDL


with open('dl.txt', "r") as f:
    lines = [line.rstrip().split('\t') for line in f]

for i in range(0, len(lines)):
    if len(lines[i]) == 1:
        lines[i].append('Clip ' + str(i + 1))

with open('failed.txt', 'w') as g:
    for i in range(0, len(lines)):
        try:
            print('Trying to download video', i + 1, 'out of', len(lines))
            filename = lines[i][1]
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
