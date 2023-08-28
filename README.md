# Updates to scripts soon, most likely aren't working atm

# Simple step-by-step guide on how to download (multiple) videos in the highest quality that has audio via yt-dlp

Please read this read-me (or at least the part that you want to use) before downloading anything and/or asking questions.
If something is unclear or not working correctly, DM me on Discord (@matz3).\
—\
Supported sites: Twitter, YouTube, Discord, Twitch, Google Drive, streamable, ... (basically every mainstream video-hosting platform). A detailed list is available [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).\
—\
The downloading-methods listed below should work on Windows 10/11, I have no clue what would need to be adjusted to make it run on Linux and/or Mac. If you know, please tell me and I'll adjust this guide accordingly.\
Also: All of this only works if the link is publicly available, i.e. you can’t download private Twitter-clips or private YouTube-videos with this method.

## Content

- [1) Downloading a single video, needs (almost) no setup](https://github.com/bttarchive/download-segments#1-downloading-a-single-video)
  - If you rarely download videos and need an all-in-solution for exactly that, use this. Very useful method if Twitter decides to shit the bed again, as yt-dlp usually has bypasses ready within hours.

- [2) Downloading multiple videos, needs almost no setup](https://github.com/bttarchive/download-segments#2-downloading-multiple-videos)
  - If you want to download multiple videos at one time and don't care about renaming them or trimming them directly, use this method.

- [3) Downloading multiple videos, renaming them and trimming the output files, needs some setup](https://github.com/bttarchive/download-segments#3-downloading-multiple-videos-renaming-them-and-trimming-the-output-files)
  - If you want to download multiple videos at one time, rename them automatically, and only download sections around given timestamps, use this method. Could be useful if you need to download a lot of segments, e.g. for a BTT-video.

- [4) Downloading multiple videos at once authorizing to a Google-Sheets-Document, needs a lot of setup](https://github.com/bttarchive/download-segments#4-downloading-multiple-videos-at-once-authorizing-to-a-google-sheets-document)
  - Only really useful if you don't want to create the .txt-file from the 2nd method and instead want to directly read the links + names from a Google-Sheets-Document.

## 1) Downloading a single video

Step 1)\
Go to https://github.com/yt-dlp/yt-dlp/releases and download the latest file that is called “yt-dlp.exe”.

Step 2) [optional]\
Move the file to a folder in which you want to store the video-files later.

Step 3)\
Open the folder with the “yt-dlp.exe” file. Then click somewhere here (where the red thing is):\
![Screenshot 1](https://i.imgur.com/gGYrlBH.png)

After clicking there it should look similar to this:\
![Screenshot 2](https://i.imgur.com/Qczpa7F.png)

Step 4)\
Type *cmd* and hit enter.

Step 5)\
Type *yt-dlp “LINK”* and hit enter (sometimes you don't need to put quotation marks around the link).

Example-Screenshot:\
![Screenshot 3](https://i.imgur.com/xwInm6j.png)

Note: If this doesn't work, try updating yt-dlp by typing *yt-dlp -U*, hitting enter and then repeating step 5). If this doesn't work as well, you can try updating to the nightly version, which is the unofficial/unstable update by typing *yt-dlp --update-to nightly*, hitting enter and then try step 5) again.

---

Alternative to Step 5) if you want to rename your video-files directly:\
Type *yt-dlp “LINK” -o ”NAME”.%(ext)s* (the last part makes sure you can open the file later).

Example-Screenshot:\
![Screenshot 4](https://i.imgur.com/1bnHUcH.png)

## 2) Downloading multiple videos

This works the same way as downloading a single video does, but instead of entering a URL in the command prompt, you enter a file-name that contains yours URLs.

Step 1)\
Go to https://github.com/yt-dlp/yt-dlp/releases and download the latest file that is called “yt-dlp.exe”.

Step 2) [optional]\
Move the file to a folder in which you want to store the video-files later.

Step 3)\
Prepare a .txt-file with 1 URL per line and save it in the same folder where the yt-dlp.exe is.

Step 4)\
Open the folder with the “yt-dlp.exe” and .txt-file. Then click somewhere here (where the red thing is):\
![Screenshot 1](https://i.imgur.com/gGYrlBH.png)

After clicking there it should look similar to this:\
![Screenshot 2](https://i.imgur.com/Qczpa7F.png)

Step 5)\
Type *cmd* and hit enter.

Step 6)\
Type *yt-dlp -a file_name.txt* and hit enter.

Example-Screenshot:\
![Screenshot 3](https://i.imgur.com/qvHlXcU.png)

Note: If this doesn't work, try updating yt-dlp by typing *yt-dlp -U*, hitting enter and then repeating step 6). If this doesn't work as well, you can try updating to the nightly version, which is the unofficial/unstable update by typing *yt-dlp --update-to nightly*, hitting enter and then try step 6) again. If this still doesn't work, you most likely provided at least 1 link that is not-downloadable, try again without that link.

## 3) Downloading multiple videos, renaming them and trimming the output files

Step 1)\
Download and install Python (https://www.python.org/downloads/). The latest version should usually work, the last one I tested that certainly works is v3.11.3.

Step 2)\
Download [this script](https://raw.githubusercontent.com/bttarchive/download-segments/main/dl.py).\
Open the link in a new tab, right-click anywhere, select “Save as…” and click Save. Make sure to select file-type "Python File" or "Any Type" (or anything that ends in .py) so that the script gets properly saved and not converted to another (unreadable) file-type.

If you do not want to automatically convert your videos to 60fps, download [this script](https://raw.githubusercontent.com/bttarchive/download-segments/main/dl2.py) instead (rename it to dl.py or use dl2.py instead of dl.py whenever mentioned).

*[2023-07-06: Added 3rd version. This version always updates to the latest unofficial yt-dlp-release, which usually includes several bugfixes that did not make it into the latest release (e.g. a workaround to download Twitter-clips).]*

Step 3) [optional]\
Move the script to a folder in which you want to store the video-files later.

Step 4) [optional]\
If you want to download parts of YouTube-videos instead of the whole videos, you need to install ffmpeg. Go to https://www.gyan.dev/ffmpeg/builds/ and download the latest file that is called “ffmpeg-git-full.7z”. After downloading it, unzip the folder, open it and go into the subfolder "bin". In there you should find 3 files (ffprobe, ffplay, ffmpeg). Move these 3 files into the folder with the script.

If you did this step, yt-dlp can now download ranges of YouTube-videos if they are timestamped, starting 5 seconds before the given timestamp and ending 85 seconds after it. If you want the clips to be a different length, specify so in the .txt-file (see next step).

Step 5)\
Create a .txt-file that contains the links to the videos you want to download (1 link per line) in the same folder. You can also include names and desired video-length (in seconds) for each video (this part only works for timestamped YouTube-videos), but both are not necessary (unnamed videos will be renamed to Clip <*number in list*>, unspecified video-length will be 90 seconds). Names and video-length have to be separated by the links using a tab (↹).\
Easy way to do this: Collect all the links on a Spreadsheet with the links in one column and the names in the column next to it (and desired video-length next to that). Copy the whole range and paste it into the .txt-file (remember: names and video-length are not necessary).

Example-Screenshot (right side shows how your .txt-file should look if it includes names and video-lengths):\
![Screenshot 5](https://i.imgur.com/fKdgFcq.png)

Important: The .txt-file has to be called/renamed to **dl.txt**, otherwise the script will not work.

Step 6)\
Open the folder with the *dl.txt* and *dl.py* files (depending on Step 4) there could be more files in your folder). Then click somewhere here (where the red thing is):\
![Screenshot 1](https://i.imgur.com/gGYrlBH.png)

After clicking there it should look similar to this:\
![Screenshot 2](https://i.imgur.com/Qczpa7F.png)

Step 7)\
Type *cmd* and hit enter.

Step 8)\
Type *dl.py* and hit enter. If you are familiar with Python you may have installed an IDE that will now open. Just run the script from there.

Note: You may find a new file in your folder called *failed.txt*. In it you can find the links to the videos that failed to download with their iterated number in the list of links and their (un-)specified name. If no videos failed to download, the file will be empty. Either way, you can delete this .txt-file if you want.\
Videos appearing in this .txt-file usually could not be accessed by yt-dlp (the video is most likely private/deleted or the link does not directly contain a video), but you can also try to download it again to make sure it's not an error (just repeat the steps above).

## 4) Downloading multiple videos at once authorizing to a Google-Sheets-Document

This is how I archive BTT-segments for the [Archive-Channel](https://www.youtube.com/@bttarchive).

Explanation hopefully soon!
