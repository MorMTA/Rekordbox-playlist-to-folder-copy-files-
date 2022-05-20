# This project was made by me after trying to move out of Rekordbox and had
# to move each one of my songs, one by one to a new playlist.
# wasn't going to do that hard work so i made this program, it recives the name each song
# looks it up in a path (for example: /Contents, a folder made by Rekordbox) and then copy it
# to a chosen destination folder.


# Instructions:
# 1. In Rekordbox, right click the chosen playlist and export to KUVO text file
# 2. open the text file with EXCEL, it will prompt some messages, keep it on deafults
# 3. copy the TRACK TITLE row to a new excel file
# 4. save it as text file with delimiters
# 5. replace the txt_file_name with your text file path\name
# 6. Enjoy!

# Note: it might not find all, but it finds at least 90% of the songs which leaves you
# with as little work as possible

# To start, activate main()

# written by: Mor Alafrangi

from codecs import decode, encode
from os.path import exists
import shutil as sh
import os

#To find a file in the system given part of file name and the path
def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        #if(len(filename)):
        for name2 in filename:
            if name in name2:
             return os.path.join(dirpath, name2)


#strips the song_name of delimiters
def stripSongName(song_name):
    song_name = song_name.strip('\t')
    song_name = song_name.strip('\n')
    song_name = song_name.strip('"')
    return song_name

def main():
    index = 1 # to check if all songs were read
    src_path = "C:/Users/User/Music" #the path to look inside of
    dest_directory_path = "C:/Users/User/Documents/Transfer songs from rekordbox program/Minimal" #the path to copy songs to
    txt_file_name = "Minimal.txt" # The text file with the name of the songs
    none = 0 # not found
    good = 0 # copied

    file = open(txt_file_name,"r")
    newFile = file.read().splitlines()
    not_found = [] # a list of all not found songs
    for line in newFile:
        song_name = line
        song_name = stripSongName(song_name)

        print(song_name)
        if(len(song_name)):
            filepath = findfile(song_name, src_path)
            print(filepath)
            if(filepath is None):
                none = none + 1
                not_found.append(song_name)
            else:
                sh.copy2(filepath,dest_directory_path)
                good = good + 1
            index = index + 1
    print(index)
    print("none = ")
    print(none)
    print(" good = ")
    print(good)
    print(not_found)

main()