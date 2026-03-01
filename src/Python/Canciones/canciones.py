liked_songs = {
    'Reloj' : 'Luis Miguel',
    'Baile inolvidable' : 'Bad Bunny',
    'Love never felt so good' : 'Michael Jackson',
    'After last night' : 'Bruno Mars'
}

def write_liked_songs_to_file(liked_songs, favs):
    with open(favs, "w", encoding="utf-8") as file:
        for song, artist in liked_songs.items():
            file.write(f"{song} by {artist}\n")

write_liked_songs_to_file(liked_songs, "favs.txt")