def make_album(artist_name, album_name, song_num=0):
    """will print album"""
    
    music = {'artist': artist_name, 'album':album_name}
    
    return music
    
while True:
    print ("Enter artist details:")
    
    artist_name = input("artist: ")
    if artist_name == 'q':
        break
    album_name = input("album: ")
    if album_name == 'q':
        break
    
    print (f"{artist_name} {album_name}")
    
    
    