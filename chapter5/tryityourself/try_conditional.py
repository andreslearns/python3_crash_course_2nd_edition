video_card = 'Nvidia'
video_card == 'nvidia'

if video_card == 'nvidia':
    print ("Is video card == nvidia? I predict True")
else:
    print (f"Well it's not!")
    
video_games = ['legend of the dragoon', 'tekken', 'final fantasy', 'street fighter']

if 'pingpong' not in video_games:
    print (f"False! Pingpong is not a video game!")
    
if 'legend of the dragoon' in video_games[:]:
    print (f"It was andrew's favorite childhood game!")
    
if 'legend of the dragoon' and 'tekken' in video_games:
    print ("What an awesome childhood!")

if 'legend of the dragoon' or 'tekken' in video_games:
    print ("Still an awesome childhood!")

if 'legend of the dragoon' and 'tekken' not in video_games:
    print ("Still an awesome childhood!")
else:
    print (f"not so awesome childhood")
    

cond = video_card.lower() == 'nvidia'

print (cond)
print (video_card)



