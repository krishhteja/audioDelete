# audioDelete
Delete audio from video files<br>

FFmpeg is required which can be downloaded from - http://ffmpeg.org/download.html <br><br>
Copy all the files into one single directory and run the script. All the edited files can be found in a newly created directory named 'edited' which is located inside the current directory.<br><br>

The equivalent shell command is 'mkdir edited; for file in *; do ffmpeg -i "$file" -c copy -an "edited/$file"; done'
