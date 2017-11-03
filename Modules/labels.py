from Modules.imports import *

ps_dir = "F:\\Scripts\\Python\\flac_to_mp3\PowerShell"


def give_labels(artist, album, songname, song_path):
    global ps_dir
    os.chdir(ps_dir)
    #artist = artist.encode('ISO-8859-1')
    #album = album.encode('ISO-8859-1')
    #songname = songname.encode('ISO-8859-1')
    #song_path = song_path.encode('ISO-8859-1')
    subprocess.call(['powershell',
                     '-ExecutionPolicy',
                     'Bypass',
                     '.\\change_labels.ps1',
                     "'{0}'".format(artist),
                     "'{0}'".format(album),
                     "'{0}'".format(songname),
                     "'{0}'".format(song_path)],
                    shell=True,
                    stdout=subprocess.PIPE)


def get_label(song_path, label_name):
    global ps_dir
    os.chdir(ps_dir)
    label_value = subprocess.Popen(['powershell',
                     '-ExecutionPolicy',
                     'Bypass',
                     '.\\get_label.ps1',
                     "'{0}'".format(song_path),
                     "'{0}'".format(label_name)],
                    shell=True, stdout=subprocess.PIPE).communicate()[0]
    return label_value.decode("utf-8")[:-2]


def get_all_labels(flac_full_path):
    artist = get_label(flac_full_path, "Artists")
    album = get_label(flac_full_path, "Album")
    songname = get_label(flac_full_path, "Title")
    return artist, album, songname


