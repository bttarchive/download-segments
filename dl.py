from __future__ import unicode_literals
import subprocess
import sys

with open('dl.txt', 'r', encoding="utf8") as e:
    offset = 0
    pp = 0
    fps = 0
    check = [line.rstrip().split('\t') for line in e]
    last_row = str(check[len(check) - 1])
    if 'OPTIONS' in last_row:
        offset = 1
        if 'CV' in last_row:
            pp = 1
        if 'UP' in last_row:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "setuptools", "wheel"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall",
                                   "https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "ffmpeg-python"])
        if 'FPS' in last_row:
            fps = 1
    else:
        print("No additional options given")

from yt_dlp import YoutubeDL
from yt_dlp.utils import download_range_func


def download_segments():
    with open('dl.txt', 'r', encoding="utf8") as f:
        lines = [line.rstrip().split('\t') for line in f]

    for i in range(0, len(lines) - offset):
        lines[i].extend(['', ''])
        if lines[i][1] == '':
            lines[i][1] = 'Clip ' + str(i + 1)

    for i in range(0, len(lines) - offset):
        if lines[i][2] == '':
            lines[i][2] = '80'

    substring1 = "youtu"
    substring2 = "t="
    substring3 = "twitch.tv/videos"

    with open('failed.txt', 'w') as g:
        for i in range(0, len(lines) - offset):
            try:
                print('Trying to download video', i + 1, 'out of', len(lines) - offset)
                filename = 'Videos/' + lines[i][1]
                link = lines[i][0]

                try:
                    if (substring1 in link) and (substring2 in link):
                        timestamp = link.split("t=", 1)[1]
                        if timestamp[-1:] == 's':
                            timestamp = timestamp[:-1]
                        start_second = max(int(timestamp) - 5, 0)
                        end_second = int(timestamp) + int(lines[i][2]) + 5
                        if pp == 1:
                            if fps == 1:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func(None, [(start_second, end_second)]),
                                    'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                    'postprocessors': [{
                                        'key': 'FFmpegVideoConvertor',
                                        'preferedformat': 'mp4'
                                    }],
                                }
                            else:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func(None, [(start_second, end_second)]),
                                    'postprocessors': [{
                                        'key': 'FFmpegVideoConvertor',
                                        'preferedformat': 'mp4'
                                    }],
                                }
                        else:
                            if fps == 1:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func(None, [(start_second, end_second)]),
                                    'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                }
                            else:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func(None, [(start_second, end_second)]),
                                }
                        with YoutubeDL(ydl_opts) as ydl:
                            ydl.download([lines[i][0]])

                    elif (substring3 in link) and (substring2 in link):
                        ts_hour = link.split("t=", 1)[1].split("h")[0]
                        ts_minute = link.split("t=", 1)[1].split("h")[1].split("m")[0]
                        ts_second = link.split("t=", 1)[1].split("h")[1].split("m")[1].split("s")[0]
                        start_ts = max(int(ts_hour)*3600 + int(ts_minute)*60 + int(ts_second) - 90, 0)
                        # Twitch VODs suck, so I hope this is enough offset to make it work
                        end_ts = int(ts_hour)*3600 + int(ts_minute)*60 + int(ts_second) + int(lines[i][2]) + 60
                        if pp == 1:
                            if fps == 1:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func([], [(start_ts, end_ts)]),
                                    'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                    'postprocessors': [{
                                        'key': 'FFmpegVideoConvertor',
                                        'preferedformat': 'mp4'
                                    }],
                                }
                            else:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func([], [(start_ts, end_ts)]),
                                    'postprocessors': [{
                                        'key': 'FFmpegVideoConvertor',
                                        'preferedformat': 'mp4'
                                    }],
                                }
                        else:
                            if fps == 1:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func([], [(start_ts, end_ts)]),
                                    'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                }
                            else:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'download_ranges': download_range_func([], [(start_ts, end_ts)]),
                                }
                        with YoutubeDL(ydl_opts) as ydl:
                            ydl.download([lines[i][0]])

                    else:
                        if pp == 1:
                            if fps == 1:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                    'postprocessors': [{
                                        'key': 'FFmpegVideoConvertor',
                                        'preferedformat': 'mp4'
                                    }],
                                }
                            else:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'postprocessors': [{
                                        'key': 'FFmpegVideoConvertor',
                                        'preferedformat': 'mp4'
                                    }],
                                }
                        else:
                            if fps == 1:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                    'downloader': 'ffmpeg',
                                    'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                }
                            else:
                                ydl_opts = {
                                    'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                              'height>720]+ba/bv*+ba/best',
                                    'format_sort': ['proto'],
                                    'outtmpl': filename + '.%(ext)s',
                                }
                        with YoutubeDL(ydl_opts) as ydl:
                            ydl.download([lines[i][0]])

                except:
                    if pp == 1:
                        if fps == 1:
                            ydl_opts = {
                                'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                          'height>720]+ba/bv*+ba/best',
                                'format_sort': ['proto'],
                                'outtmpl': filename + '.%(ext)s',
                                'downloader': 'ffmpeg',
                                'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                                'postprocessors': [{
                                    'key': 'FFmpegVideoConvertor',
                                    'preferedformat': 'mp4'
                                }],
                            }
                        else:
                            ydl_opts = {
                                'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                          'height>720]+ba/bv*+ba/best',
                                'format_sort': ['proto'],
                                'outtmpl': filename + '.%(ext)s',
                                'postprocessors': [{
                                    'key': 'FFmpegVideoConvertor',
                                    'preferedformat': 'mp4'
                                }],
                            }
                    else:
                        if fps == 1:
                            ydl_opts = {
                                'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                          'height>720]+ba/bv*+ba/best',
                                'format_sort': ['proto'],
                                'outtmpl': filename + '.%(ext)s',
                                'downloader': 'ffmpeg',
                                'downloader_args': {'ffmpeg': ['-filter:v', 'fps=60', '-vcodec', 'h264']},
                            }
                        else:
                            ydl_opts = {
                                'format': 'bv*[fps>30][height>720]+ba/bv*[fps>30][height<=720]+ba/bv*['
                                          'height>720]+ba/bv*+ba/best',
                                'format_sort': ['proto'],
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


download_segments()
