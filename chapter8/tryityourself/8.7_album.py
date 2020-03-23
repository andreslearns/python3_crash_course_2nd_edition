def make_album(artist_name, album_name, song_num=0):
    """will print album"""
    
    music = {'artist': artist_name, 'album':album_name}
    
    if song_num:
        music['tracks'] = song_num
    return music

musikero = make_album ('eraserheads','cutterpillow')
print (musikero)
musikero = make_album ('parokya ni edgar','inuman sessions',song_num = 23)
print (musikero)
musikero = make_album('metallica', 'ride the lightning')
print (musikero)
