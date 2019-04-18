# audioDelete
Delete audio from video files

FFmpeg is required which can be downloaded from - http://ffmpeg.org/download.html
Copy all the files into one single directory and run the script. All the edited files can be found in a newly created directory named 'edited' which is located inside the current directory.

The equivalent shell command is 'mkdir edited; for file in *; do ffmpeg -i "$file" -c copy -an "edited/$file"; done'
