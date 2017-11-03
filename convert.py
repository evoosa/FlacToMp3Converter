from Modules.imports import *
from Modules.functions import create_mp3_album

#print(subprocess.check_output("whoami", shell=True))

music_dir = "F:\\Music"
artist = "grandbrothers"
album = "Open"
album_dir = os.path.join(music_dir, artist, album)

print("Le Starting .")
create_mp3_album(music_dir, artist, album)
print("Le Done .")

