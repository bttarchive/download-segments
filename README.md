# Simple step-by-step guide on how to download (multiple) videos in the highest quality that has audio via yt-dlp

Please read this read-me (or at least the part that you want to use) before downloading anything and/or asking questions.
If something is unclear or not working correctly, DM me on Discord (@Matze#7132).

—

Supported sites: Twitter, YouTube, Discord, Twitch, Google Drive, streamable, ... (basically every mainstream video-hosting platform). A detailed list is available [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

—

The downloading-methods listed below should work on Windows 10/11, I have no clue what would need to be adjusted to make it run on Linux and/or Mac. If you know, please telle me and I'll adjust this guide accordingly.

Also: All of this only works if the link is publicly available, i.e. you can’t download private Twitter-Clips or private YouTube-videos with this method.

## Content

- [Downloading a single video, needs (almost) no setup](https://github.com/bttarchive/download-segments#downloading-a-single-video)

- [Downloading multiple videos at once, needs some setup](https://github.com/bttarchive/download-segments#downloading-multiple-videos-at-once)

- [Downloading multiple videos at once authorizing to a Google-Sheets-Document, needs the most setup](https://github.com/bttarchive/download-segments#downloading-multiple-videos-at-once-authorizing-to-a-google-sheets-document)

## Downloading a single video

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
![Screenshot 3](https://i.imgur.com/poCle5k.png)

---

Alternative to Step 5), if you want to rename your video-files:\
Type *yt-dlp “LINK” -o <NAME.FILE-FORMAT>*

Example-Screenshot:\
![Screenshot 4](https://i.imgur.com/OjtUaSS.png)

This downloads the full YouTube-Video and renames it to “ruined_tas.mp4”.

Important: You have to specify a file-format (in this case .mp4), otherwise you won’t be able to open the file later. Other video-file-formats work just as fine (.mov, .wmv, …)

## Downloading multiple videos at once

Step 1)\
Download and install Python (https://www.python.org/downloads/). The latest version should usually work, the last one I tested that certainly works is v3.11.3.

Step 2)\
Download [this script](https://raw.githubusercontent.com/bttarchive/download-segments/main/dl.py).\
Right-click anywhere, select “Save as…” and click Save. Make sure to select file-type "Any Type" (or anything thats end in .py) so that the script gets properly saved and not converted to another file-type.

Step 3) [optional]\
Move the script to a folder in which you want to store the video-files later.

Step 4)\
Create a .txt-file that contains the links to the videos you want to download (1 link per line) in the same folder. You can also include names for each video, but that’s not necessary (unnamed videos will be renamed to Clip <n>). Names have to be separated by the links using a tab (↹).\
Easy way to do this: Collect all the links on a Spreadsheet with the links in 1 column and the names in the column next to it. Copy the whole range and paste it into the .txt-file (remember: names are not necessary).

Example-Screenshot (right side shows how your .txt-file should look):\
![Screenshot 5](https://i.imgur.com/qJvHc1w.png)

Important: The .txt-file has to be called/renamed to **dl.txt**, otherwise the script will not work.

Step 5)\
Open the folder with the *dl.txt* file. Then click somewhere here (where the red thing is):\
![Screenshot 1](https://i.imgur.com/gGYrlBH.png)

After clicking there it should look similar to this:\
![Screenshot 2](https://i.imgur.com/Qczpa7F.png)

Step 6)\
Type *cmd* and hit enter.

Step 7)\
Type *dl.py* and hit enter. If you are familiar with Python you may have installed an Interpreter that will now open. Just run the script from there.

Note: If some links failed to download, you will find a new file in your folder, called failed.txt. In it you can find the links to the videos that failed to download with their iterated number in the list of links and their (un-)specified name.\
In most cases that means that yt-dlp could not access the link/video (it’s most likely private/deleted or the link does not directly contain a video), but you can also try to download it again to make sure (just repeat the steps above).

## Downloading multiple videos at once authorizing to a Google-Sheets-Document

soon
