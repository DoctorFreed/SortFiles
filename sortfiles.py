# TODO Сделать логирование, что куда было перемещено
# TODO Найти способ справляться с дубликатами
# TODO Сделать для программы GUI на QT

import json
import os
import argparse

PATERN_EXT = {
    'Audio': ['.mp3', '.aac', '.flac', '.m4r', '.ogg', '.wav', '.m4p', '.m4b', '.m4a'],
    'Images': ['.png', '.jpg', '.jpeg', '.webp', '.gif', '.ico', '.psd'],
    'Documents': ['.doc', '.pdf', '.txt', '.xlsx', '.pptx', '.docx', '.ppt', '.xls', '.ini'],
    'Torrents': ['.torrent'],
    'Archives': ['.gz', '.tar', '.zip', '.rar', '.7z'],
    'Video': ['.mp4', '.flv', '.avi', '.mkv', '.mov', '.webm'],
    'Soft': ['.exe', '.msi'],
    'Source Code': {'C++': ['.cpp'], 'Python': ['.py']}
}

#M_DIR = 'C:\\Users\\roman\\Downloads\\'


def parse_args():
    parser = argparse.ArgumentParser(
        description='SortFiles - script for sorting your files \n'
        'https://github.com/DoctorFreed/SortFiles'
    )
    parser.add_argument('folder', help='Specify the folder where'
                        ' the files will be sorted', type=str)
    parser.add_argument('-j', '--json', help='The path to the json file,'
                        ' if the argument is not specified,'
                        ' the patern.json file will be used.'
                        ' If there is no file, the pattern that is already'
                        ' in the code will be used.', type=str, default='')
    parser.add_argument('-u', '--unknown', help='by specifying this argument,'
                        ' unknown formats will '
                        ' be sorted into the "UNKNOWN" folder.'
                        ' By default, this sorting '
                        ' does not occur.', action='store_true')

    args = parser.parse_args()
    return args


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
    def __init__(self, files: list, unknown_mode=False) -> None:
        self.__files = files
        self.__unknown_mode = unknown_mode

    def search_path(self, paterns: dict, ext: str, old='') -> str:
        for p in paterns:
            if isinstance(paterns[p], list) and ext in paterns[p]:
                return old + '\\' + str(p) + '\\'
            elif isinstance(paterns[p], dict):
                return old + self.search_path(paterns[p], ext, str(p))
            else:
                continue

    def sorting(self) -> None:
        for file in self.__files:
            try:
                path_to_sort = self.search_path(PATERN_EXT, file.ext)
            except:
                if self.__unknown_mode:
                    path_to_sort = 'UNKNOWN' + '\\'
                else:
                    continue
            if not os.path.isdir(file.path_folder + path_to_sort):
                os.makedirs(file.path_folder + path_to_sort)
            try:
                os.rename(
                    file.full_path, file.path_folder + '\\' + path_to_sort + file.name
                )
            except:
                print(file.name, 'Error!')


def json_pars(path='patern.json') -> None:
    if os.path.isfile(path):
        with open(path, 'w') as file:
            json.dump(PATERN_EXT, file)
    else:
        print('File', path, 'does not exist')


def main():
    args = parse_args()
    if args.json:
        json_pars(args.json)
    m_dir = args.folder + '\\'
    files_raw = os.listdir(m_dir)
    files = []
    for file in files_raw:
        if os.path.isfile(m_dir + '\\' + file):
            files.append(File(file, m_dir))
    s = Sort(files, args.unknown)
    s.sorting()


if __name__ == "__main__":
    main()
