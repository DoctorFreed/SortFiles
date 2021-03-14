# TODO: задокументируй код!

import json
import os
import argparse
import logging
from random import randint

# ---------------------------------------------------------------------------
#   Pattern for sorting if the json file is not detected
# ---------------------------------------------------------------------------
TEMPLATE_EXT = {
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
    '[%(levelname)s] (%(asctime)s) : %(funcName)s : %(message)s')
format_logger_info = logging.Formatter('(%(asctime)s) - %(message)s')


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

# ---------------------------------------------------------------------------
#   Parsing command line arguments
# ---------------------------------------------------------------------------


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
                        ' the template.json file will be used.'
                        ' If there is no file, the template that is already'
                        ' in the code will be used.', type=str, default='')
    parser.add_argument('-u', '--unknown', help='by specifying this argument,'
                        ' unknown formats will '
                        ' be sorted into the "UNKNOWN" folder.'
                        ' By default, this sorting '
                        ' does not occur.', action='store_true')
    parser.add_argument('-d', '--debug', help='writes all the work of the script'
                        ' to the debug.log file', action='store_true')
    parser.add_argument('-l', '--log', help='writes to the info.log file about where'
                        ' the files were moved to', action='store_true')

    args = parser.parse_args()
    logger.debug('Parsing passed, return args')
    return args

# ---------------------------------------------------------------------------
#   Implementation of the File class
# ---------------------------------------------------------------------------


class File:
    """
    A class used to store information about a file

    ...

    Attributes
    ----------
    name : str
        file name and extension
    path_folder : str
        the folder where the file is located
    full_path : str
        full path to the file
    ext : str
        file extension
    clear_name : str
        file name without extension
    """

    def __init__(self, name: str, path_folder: str) -> None:
        """

        Parameters
        ----------
        name : str
            File name
        path_folder : str
            The folder where the file is located
        """
        self.__name = name
        self.__path_folder = path_folder
        self.__full_path = path_folder + '\\' + name
        self.__ext = os.path.splitext(self.__full_path)[1].lower()
        self.__clear_name = os.path.splitext(name)[0]
        logger.debug('An object of the File type was created. \n'
                     'Name : {} \nPath Folder : {} \nFull Path : {}'.format(
                         self.__name, self.__path_folder, self.__full_path
                     )+'\nExt : {} \nClear Name : {}'.format(
                         self.__ext, self.__clear_name))

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

# ---------------------------------------------------------------------------
#   Implementation of the Sort class
# ---------------------------------------------------------------------------


class Sort:
    """
    Class for sorting files

    ...

    Attributes
    ----------
    files : list
        list of files to sort
    unknown_mode : bool
        A mode in which unknown extensions will be placed in the UNKNOWN folder(default False)

    Methods
    -------
    search_path(paterns: dict, ext: str, old='') -> str
        Finding the path to sort the file
    rename_file(file: File, new_name='') -> str
        Renaming a file
    sorting() -> None
        Sorting all files in an object
    """

    def __init__(self, files: list, unknown_mode=False) -> None:
        """

        Parameters
        ----------
        files: list
            list of files to sort
        unknown_mode : bool, optional
            A mode in which unknown extensions will be placed in the UNKNOWN folder(default False)
        """
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
            new_name = new_name + file.ext
        logger.debug('File renaming completed, return {}'.format(new_name))
        return new_name

    def sorting(self) -> None:
        logger.debug('Start sorting files')
        for file in self.__files:
            try:
                logger.debug(
                    '{} - looking for a sorting path in the template'.format(file.name))
                path_to_sort = self.search_path(TEMPLATE_EXT, file.ext)
            except:
                logger.error(
                    '{} - has an unknown extension {}'.format(file.name, file.ext))
                if self.__unknown_mode:
                    logger.debug(
                        'Unknown mode is enabled, the file will be moved to this folder')
                    path_to_sort = 'UNKNOWN' + '\\'
                else:
                    logger.debug(
                        'Unknown mode is disabled, the file will not be moved')
                    continue
            logger.debug('Checking for the existence of a folder - {}'
                         .format(file.path_folder + path_to_sort))
            if not os.path.isdir(file.path_folder + path_to_sort):
                os.makedirs(file.path_folder + path_to_sort)
                logger.debug('Folder {} was created'.format(
                    file.path_folder + path_to_sort))
            new_path = file.path_folder + '\\' + path_to_sort + file.name
            try:
                logger.debug('Attempt to move a file to a new location')
                os.rename(
                    file.full_path, new_path
                )
                logger.info('File [{}] moved to [{}]'.format(
                    file.full_path, new_path))
            except:
                logger.error('File [{}] transfer Error'.format(file.name))
                if os.path.isfile(new_path):
                    logger.error('File [{}] is already exist, rename it.'
                                 .format(file.name))
                    new_name = self.rename_file(file)
                    logger.debug('Attempt to move a file to a new location')
                    new_path = file.path_folder + '\\' + path_to_sort + new_name
                    logger.debug('Transferring a file [{}] move to [{}]'
                                 .format(file.full_path, new_path))
                    os.rename(file.full_path, new_path)
                else:
                    logger.error(
                        'The file could not be transferred in any way')

# ---------------------------------------------------------------------------
#   Function for configuring a template by JSON
# ---------------------------------------------------------------------------


def json_pars(path='template.json') -> None:
    logger.debug('Configuring a JSON template')
    if os.path.isfile(path):
        logger.debug('The transferred file exists,'
                     ' it is being written to the dictionary')
        with open(path, 'w') as file:
            json.dump(TEMPLATE_EXT, file)
        logger.debug('The dictionary is ready to use')
    else:
        logger.error('File {} does not exist'.format(path))
        logger.debug('We use a ready-made template')

# ---------------------------------------------------------------------------
#   Running the script
# ---------------------------------------------------------------------------


def main():
    args = parse_args()
    if args.json:
        json_pars(args.json)
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('The logging level is set to DEBUG')
        logger_debug_setup()
    if args.log:
        logger.debug('The argument for enabling log is specified')
        logger_info_setup()
    m_dir = args.folder + '\\'
    logger.debug(
        'The main directory [{}] for sorting is installed'.format(m_dir))
    files_raw = os.listdir(m_dir)
    logger.debug('All files in the folder are received')
    logger.debug(files_raw)
    files = []
    for file in files_raw:
        if os.path.isfile(m_dir + '\\' + file):
            files.append(File(file, m_dir))
    logger.debug('Files : {}'.format(files))
    logger.debug('Number of files : {}'.format(len(files)))
    s = Sort(files, args.unknown)
    s.sorting()


if __name__ == "__main__":
    main()
