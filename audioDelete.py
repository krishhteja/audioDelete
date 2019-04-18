import subprocess

command = 'mkdir edited; for file in *; do ffmpeg -i "$file" -c copy -an "edited/$file"; done'

subprocess.call(command, shell=True)
