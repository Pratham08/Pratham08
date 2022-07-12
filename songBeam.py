#create playlist and play music
import sys
import os
import time
import pygame
from pygame.mixer import get_busy

def playPlaylist(filename):
    f = open(filename,'r')
    song_string = f.read()
    songs = song_string.split('\n')
    f.close()
    pygame.init()
    for i in range(len(songs)-1):
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play()
        while True:
            if pygame.mixer.music.get_busy() == False:
                break
        pygame.mixer.music.unload()
    pygame.quit()
    
def editPlaylist(filename):
    try: 
        f = open(filename,'r')
        print('Songs listed in '+filename+':')
        fstr = f.read()
        num_songs = fstr.count('\n')
        f.close()
        f = open(filename,'r')
        for i in range(num_songs):
          print(i+1,end='')
          print('. ' + f.readline(),end='')
        f.close()
        f = open(filename,'a')
        n_song = input('\nEnter the name of the song to be added: ')
        f.write(n_song)
        f.close()
        print('Succesfully added the song..')
        time.sleep(1)
        exit()
    except:
        #print('Error occured while handling your files..')
        print('')

def createPlaylist(filename):
    try:
        print('Enter the names of the song files you want to add: ')
        songlist = []
        i = 0
        while True:
            song_name = input()
            if song_name == 'done':
                break
            else:
                songlist.append(song_name)
                i+=1
        #create new file now
        f = open(filename,'w')
        for j in range(len(songlist)):
            f.write(songlist[j] + '\n')
        f.close()
        print('All songs successfully added..')
        time.sleep(1)
        exit()
    except:
        #print('Some error occured')
        print('')

def createOrEditPlaylist():
    print('***Welcome to SongBeam***')
    print('As you didn\'t enter any playlist name, it is assumed that you want to create or edit a playlist...')
    print('If you didnt intented to do this.. enter \'python main.py help\' to open help menu..')
    ans = input('Enter name of a playlist: ')
    filename = ans+'.txt'
    if os.path.exists(ans+'.txt'):
        print('The entered playlist name already exists..')
        print('Entering editing mode..')
        editPlaylist(filename)
    else:
        print('Creating a new playlist..')
        createPlaylist(filename)

#print(str(sys.argv))
arglist = str(sys.argv)

if len(sys.argv) == 1:
    createOrEditPlaylist()
elif len(sys.argv) == 2:
    playPlaylist(sys.argv[1]+'.txt')
else:
    if int(sys.argv[2])==0 or int(sys.argv[2]==1):
        playPlaylist(sys.argv[1]+'.txt')
    else:
        for i in range(int(sys.argv[2])):
            playPlaylist(sys.argv[1]+'.txt')



