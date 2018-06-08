from Modules.imports import *
from Modules.FileRelated import create_mp3_album, create_mp3_all
from Modules import config

music_dir = input("Music Directory PLS: ")
#music_dir = "{partition}\\Music".format(partition=config.PARTITION)

print("Le Starting .")
create_mp3_all(music_dir)
print("Le Done .")
