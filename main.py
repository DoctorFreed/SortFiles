import os

PATERN_EXT = {
    'Audio' : ['.mp3', '.aac', '.flac', '.m4r', '.ogg', '.wav', '.m4p', '.m4b', '.m4a'],
    'Images' : ['.png', '.jpg', '.jpeg', '.webp', '.gif', '.ico', '.psd'],
    'Documents' : ['.doc', '.pdf', '.txt', '.xlsx', '.pptx', '.docx', '.ppt', '.xls', '.ini'],
    'Torrents' : ['.torrent'],
    'Archives' : ['.gz', '.tar', '.zip', '.rar', '.7z'],
    'Video' : ['.mp4', '.flv', '.avi', '.mkv', '.mov', '.webm'],
    'Soft' : ['.exe', '.msi'],
    'Source Code' : ['.cpp', '.py']
}

M_DIR = 'C:\\Users\\roman\\Downloads' 

class File:
    def __init__(self, name: str, path_folder: str) -> None:
        self.__name = name
        self.__path_folder = path_folder
        self.__full_path = path_folder + '\\' + name
        self.__ext = os.path.splitext(self.__full_path)[1].lower()
    
    @property
    def name(self):
        return self.__name
    
    @property
    def path_folder(self):
        return self.__path_folder
    
    @property
    def full_path(self):
        return self.__full_path
    
    @property
    def ext(self):
        return self.__ext

class Sort:
    def __init__(self, files: list) -> None:
        self.__files = files
    
    def sorting(self):
        for file in self.__files:
            for cat in PATERN_EXT:
                if file.ext in PATERN_EXT[cat]:
                    if not os.path.isdir(file.path_folder + '\\' + cat):
                        os.mkdir(file.path_folder + '\\' + cat)
                    try:
                        os.rename(file.full_path, file.path_folder + '\\' + cat + '\\' + file.name)
                    except:
                        print('Error file : ', file.name)

        
files_raw = os.listdir(M_DIR)
files = []
for file in files_raw:
    if os.path.isfile(M_DIR + '\\' + file):
        files.append(File(file, M_DIR))
srt = Sort(files)
srt.sorting()
        

# files = os.listdir(m_dir)
# for file in files:
#     full_name = os.path.basename(
#         m_dir + '\\' + file)
#     ext = os.path.splitext(full_name)[1].lower()
#     for cat in patern:
#         if ext in patern[cat]:
#             if not os.path.isdir(m_dir + '\\' + cat):
#                 os.mkdir(m_dir + '\\' + cat)
#             try:
#                 os.rename(m_dir + '\\' + file, m_dir + '\\' + cat + '\\' + file)
#             except:
#                 print('Error file : ', file)