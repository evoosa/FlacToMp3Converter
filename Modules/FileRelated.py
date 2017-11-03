from Modules.imports import *


def has_flac(album_dir):
    """
    If it finds a FLAC file in the album_dir,
    creates a new album-mp3 directory and retuerns True.
    else - return False.
    """
    for file_ in os.listdir(album_dir):
        if file_.endswith(".flac"):
            return True
    return False


def create_mp3_file(album_dir, flac_file, new_folder_path):
    """
    creates a single MP3 file in the new album folder.
    """
    flac_full_path = os.path.join(album_dir, flac_file)
    file_name = flac_file[:-5]
    flac = AudioSegment.from_file(flac_full_path, "flac")
    mp3_full_path = os.path.join(new_folder_path, "{0}.mp3".format(file_name))
    flac.export(mp3_full_path, format="mp3")
    labels = get_all_labels(flac_full_path)
    give_labels(labels[0], labels[1], labels[2], mp3_full_path)


def create_mp3_album(log, music_dir, artist, album):
    """
    Creates a MP3 album from the FLAC album, if it has FLAC files in it.
    """
    flac_album_dir = os.path.join(music_dir, artist, album)
    if has_flac(flac_album_dir) == True:
        print(artist + "  -  " + album)
        log.write(artist + "  -  " + album + "\n")
        new_folder_path = os.path.join(flac_album_dir, "..\\{0}-mp3".format(album))
        if os.path.exists(new_folder_path) == False:
            os.mkdir(new_folder_path)
            flac_album_folder_contents = os.listdir(flac_album_dir)
            for flac_file in flac_album_folder_contents:
                if flac_file.endswith(".flac"):
                    create_mp3_file(flac_album_dir, flac_file, new_folder_path)


def create_mp3_all(music_dir):
    log = open("F:\\Scripts\\Python\\flac_to_mp3\\log.txt", "w")
    artists = os.listdir(music_dir)
    for artist in artists:
        artist_dir = os.path.join(music_dir, artist)
        if os.path.isdir(artist_dir):
            albums = os.listdir(artist_dir)
            for album in albums:
                album_dir = os.path.join(artist_dir, album)
                if os.path.isdir(album_dir):
                    create_mp3_album(log, music_dir, artist, album)
    log.close()


