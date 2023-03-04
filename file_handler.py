import sys
import os
import time
from chardet.universaldetector import UniversalDetector
import dst
import FSM_2

t = tags.Tags()

closed_t, unclosed_t = t.tags()
# print(closed_t)
# print(unclosed_t)


def platform():
    """Returns the platform name for filesystem-based processes(Unix-like, Windows)"""
    platform = os.name
    if platform == 'nt':
        sep = '\\'
    else:
        sep = '/'
    return sep

def file_encoding(file):
    #invoking Universal Detector from chardet
    universaldetector = UniversalDetector()
    
    #opening the file in bytes mode
    f = open(file, 'rb')

    #getting file descriptor of the open file
    fd = f.fileno()

#setting the file pos at the beginning of the file
    os.lseek(fd, 0, 0)


    #Getting file attrs
    file_attrs = os.fstat(fd)

    file_size = file_attrs.st_size #Getting file size
    file_pos = 0

    while f.tell() != file_size:
        st_r = os.read(fd, file_pos)
        universaldetector.feed(st_r)
        if universaldetector.done:
            break
        file_pos = file_pos + 1
    universaldetector.close()
    return universaldetector.result





def file_reader():

    #stack stores html tags
    tags_Stack = dst.Stack()

    #prints out the pwd
    print(f"Your Current Working Dir is :: {os.getcwd()}\n")

    #gets file name
    f_name = input("Please Enter the File Name that needs checking:: ")

    #Character set that should be ignored
    ignore_char_set = [' ', '\n']

    try:
        base_dir = os.getcwd() #Getting base Dir
        sep = platform() #getting os 

        #setting up the file path
        file_path = base_dir + sep + f_name

        #opening the file
        with open(file_path, 'r') as file:
            fd = file.fileno() #Getting file descriptor
            file_stats = os.fstat(fd) #Getting file stats
            
            #getting file encoding
            detector_results = file_encoding(file_path)
            encoding = detector_results["encoding"]


            

            os.lseek(fd, os.SEEK_CUR, os.SEEK_SET)

           


            

        sys.exit(0)
        #Exit code 0
    except FileNotFoundError:
        print("File Not Found\nExiting")
        sys.exit(-1)
if __name__ == "__main__":
    file_reader()



    
    
