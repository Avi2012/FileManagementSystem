

import os
import shutil
# Documents
Documents_And_Text_Files = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".rtf", ".odt", ".tex", ".csv"]

# Images
Images = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".eps", ".ico", ".raw", ".webp"]

# Audio 
Audio = [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".midi", ".amr", ".ac3"]

# Video
Video = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".mpg", ".mpeg", ".flv", ".webm", ".vob", ".m4v", ".3gp", ".dat"]

# Programming and Executable Files
Programming_And_Executable_Files = [".exe", ".dll", ".py", ".java", ".html", ".cpp", ".c", ".php", ".rb", ".sh", ".bat", ".cmd"]

# Database
Database = [".sql", ".mdb", ".db", ".sqlite", ".xlsx", ".accdb", ".dbf", ".csv"]

# Web-related Files
Web_Related_Files = [".html", ".htm", ".css", ".js", ".php", ".asp", ".jsp", ".json", ".xml", ".rss", ".atom"]

# System Files
System_Files = [".dll", ".sys", ".ini", ".cfg", ".log", ".bat", ".cmd", ".reg", ".dll", ".sys", ".cfg", ".log", ".ini", ".bat", ".cmd"]

# Miscellaneous
Miscellaneous = [".iso", ".csv", ".xml", ".json", ".torrent", ".dat", ".bak", ".hex", ".crx", ".gz", ".tar", ".zip", ".rar", ".7z"]




path = "C:\\Users\\avi22\\Downloads"

for file_name in os.listdir(path):
    ext = os.path.splitext(file_name)[1]
    src = os.path.join(path, file_name)
    if ext in Documents_And_Text_Files:
        print(f'This file ({file_name}) is a document or text file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Documents_And_Text_Files')
        pass
    elif ext in Images:
        print(f'This file ({file_name}) is an image.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Images')
        pass
    elif ext in Audio:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Audio')
        pass
    elif ext in Video:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Video')
        pass
    elif ext in Programming_And_Executable_Files:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Programming_And_Executable_Files')
        pass
    elif ext in Database:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Database')
        pass
    elif ext in Web_Related_Files:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Web_Related_Files')
        pass
    elif ext in System_Files:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\System_Files')
        pass
    elif ext in Miscellaneous:
        print(f'This file ({file_name}) is an audio file.')
        shutil.move(src, 'C:\\Users\\avi22\\OneDrive\\Desktop\\Sorted Files\\Miscellaneous')
        pass
    else:
        print(f'This file ({file_name}) is not in any specified category.')
        pass
