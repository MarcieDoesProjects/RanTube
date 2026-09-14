from Data import def random_messages_lists():
def sublements():
    Music_sub = (random.choice(list_music_messages))
    Video_sub = (random.choice(list_video_messages))
    Suprise_sub = (random.choice(list_suprise_message))
    Bye_sub = (random.choice(list_bye_messages))
    return Bye_sub, Suprise_sub, Video_sub, Music_sub

Music_sub, Video_sub, Suprise_sub,  Bye_sub = sublements()
 
 print(F"1: {Music_sub} ")