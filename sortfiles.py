import json
import os
import argparse
import logging
from random import randint

# ---------------------------------------------------------------------------
#   Pattern for sorting if the json file is not detected
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
#   Logging setup
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)
format_logger_debug = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(funcName)s : %(message)s')
format_logger_info = logging.Formatter('%(asctime)s : %(message)s')


def logger_debug_setup() -> None:
    file_debug = logging.FileHandler('debug.log')
    file_debug.setLevel(logging.DEBUG)
    file_debug.setFormatter(format_logger_debug)
    logger.addHandler(file_debug)


def logger_info_setup() -> None:
    file_info = logging.FileHandler('info.log')
    file_info.setLevel(logging.INFO)
    file_info.setFormatter(format_logger_info)
    logger.addHandler(file_info)

# Parsing command-line arguments


def parse_args():
    logger.debug('start parsing command line arguments')
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
    parser.add_argument('-d', '--debug', help='', action='store_true')
    parser.add_argument('-l', '--log', help='', action='store_true')

    args = parser.parse_args()
    logger.debug('Parsing passed, return args')
    return args


class File:
    def __init__(self, name: str, path_folder: str) -> None:
        self.__name = name
        self.__path_folder = path_folder
        self.__full_path = path_folder + '\\' + name
        self.__ext = os.path.splitext(self.__full_path)[1].lower()
        self.__clear_name = os.path.splitext(name)[0]
        logger.debug('An object of the File type was created. \n'
                     'Name : {} \nPath Folder : {} \nFull Path : {} \nExt : {} \nClear Name : {}'
                     .format(self.__name, self.__path_folder,
                             self.__full_path, self.__ext, self.__clear_name))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name + self.__ext

    @property
    def path_folder(self):
        return self.__path_folder

    @property
    def full_path(self):
        return self.__full_path

    @property
    def ext(self):
        return self.__ext

    @property
    def clear_name(self):
        return self.__clear_name


class Sort:
    def __init__(self, files: list, unknown_mode=False) -> None:
        self.__files = files
        self.__unknown_mode = unknown_mode
        logger.debug('An object of the Sort type was created. \n'
                     'UNKNOW MODE = {}'.format(self.__unknown_mode))

    def search_path(self, paterns: dict, ext: str, old='') -> str:
        logger.debug('The dictionary is being crawled to find the path')
        for p in paterns:
            if isinstance(paterns[p], list) and ext in paterns[p]:
                logger.debug('Returning the path for sorting : {}'.format(
                    old + '\\' + str(p) + '\\'))
                return old + '\\' + str(p) + '\\'
            elif isinstance(paterns[p], dict):
                logger.debug('Checking the following dictionary')
                return old + self.search_path(paterns[p], ext, str(p))
            else:
                continue

    def rename_file(self, file: File, new_name='') -> str:
        logger.debug('Renaming the file: {}'.format(file.name))
        if not new_name:
            new_name = file.clear_name + \
                '(copy {})'.format(randint(1, 1000)) + file.ext
            logger.debug('New name file: {}'.format(new_name))
        else:
            # TODO сделать проверку на точно такое же имя, проверить написали ли расширение
            new_name = new_name + file.ext
        logger.debug('File renaming completed')
        return new_name

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
            new_path = file.path_folder + '\\' + path_to_sort + file.name
            try:
                os.rename(
                    file.full_path, new_path
                )
                logger.info('File : {} sort to {}'.format(file.full_path, new_path))
            except:
                if os.path.isfile(new_path):
                    print('File', file.name, 'is already exist, rename it.')
                    new_name = self.rename_file(file)
                    new_path = file.path_folder + '\\' + path_to_sort + new_name
                    os.rename(file.full_path, new_path)
                else:
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
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger_debug_setup()
    if args.log:
        logger.setLevel(logging.INFO)
        logger_info_setup()
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
