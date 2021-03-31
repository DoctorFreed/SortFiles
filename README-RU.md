<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/DoctorFreed/SortFiles">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SortFiles</h3>

  <p align="center">
     скрипт для сортировки файлов
    <br />
    <a href="https://github.com/DoctorFreed/SortFiles"><strong>Просмотреть документацию »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DoctorFreed/SortFiles">Демо</a>
    ·
    <a href="https://github.com/DoctorFreed/SortFiles/issues">Сообщить об ошибке</a>
    ·
    <a href="https://github.com/DoctorFreed/SortFiles/issues">Попросить "фичу"</a>
    
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Содержание</h2></summary>
  <ol>
    <li>
      <a href="#О-Проекте">О Проекте</a>
      <ul>
        <li><a href="#Требования">Требования</a></li>
      </ul>
    </li>
    <li>
      <a href="#Начало-работы">Начало работы</a>
      <ul>
      <li><a href="#Необходимые-компоненты">Необходимые компоненты</a></li>
        <li><a href="#Установка">Установка</a></li>
      </ul>
    </li>
    <li><a href="#Использование">Использование</a></li>
    <li><a href="#Карта-проекта">Карта проекта</a></li>
    <li><a href="#Участие-в-разработке">Участие в разработке</a></li>
    <li><a href="#Лицензия">Лицензия</a></li>
    <li><a href="#Контакты">Контакты</a></li>
    <li><a href="#Благодарность">Благодарность</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## О Проекте

Данный проект был создан с целью уменьшения мусора из файлов в папках, куда обычно я все кидал. Автоматическая сортировка конечно тривиальная задача, лично я хотел что бы этот процесс был максимально гибкий и удобный, поэтому и решил что правила сортировки можно менять через json файл, в будущем я обязательно добавлю GUI клиент для сортировки, а так же GUI для редактирования правил сортировки в файле json. Но даже так, ниже вы найдете инструкцию как отредактировать json файл в ручную с помощью вашего редактора текста.


### Требования

* [Python 3](https://www.python.org/downloads/)




<!-- GETTING STARTED -->
## Начало работы

Что бы запустить скрип, следуйте следующим шагам.

### Необходимые компоненты

Вам нужно установить Python 3:

* Windows 10

  1. Перейдите на офицальный сайт Python, в раздел скачивания [по этой ссылке](https://www.python.org/downloads/), скачайте и установите python 3.
        

* Ubuntu/Debian/Fedora и т.д. : python уже установлен


### Установка

1. Склонируйте репозиторий
   ```sh
   git clone https://github.com/DoctorFreed/SortFiles.git
   ```
   или скачайте ZIP архив с исходным кодом
   ![Clone repo](./images/clone.jpg)
2. Запустите скрипт в консоли
   ```sh
   python sortfiles.py -h
   ```



<!-- USAGE EXAMPLES -->
## Использование
Для начала воспользуйтесь встроеной документацией, напечатав в консоль следующуюю команду:
```sh
python sortfiles.py -h

usage: sortfiles.py [-h] [-j JSON] [-u] [-d] [-l] folder

SortFiles - script for sorting your files https://github.com/DoctorFreed/SortFiles

positional arguments:
  folder                Specify the folder where the files will be sorted

optional arguments:
  -h, --help            show this help message and exit
  -j JSON, --json JSON  The path to the json file, if the argument is not specified, the template.json file will be used. If there is no file, the   
                        template that is already in the code will be used.
  -u, --unknown         by specifying this argument, unknown formats will be sorted into the "UNKNOWN" folder. By default, this sorting does not     
                        occur.
  -d, --debug           writes all the work of the script to the debug.log file
  -l, --log             writes to the info.log file about where the files were moved to
```
Вы можете использовать разные режимы по отдельности, или скомбинировать их вместе!

Стандартное использование скрипта:
```sh
python sortfiles.py C:\MyFolder
```


_Для больших примеров просмотрите документацию [Документация](https://example.com)_



<!-- ROADMAP -->
## Карта проекта

Откройте [Issues](https://github.com/DoctorFreed/SortFiles/issues) получите список будующих функций проекта.



<!-- CONTRIBUTING -->
## Участие в разработке

Вклад в разработку - это то, что делает сообщество разработки с открытым исходным кодом, таким удивительным местом, где можно учиться, вдохновлять и творить. Любой вклад, который вы делаете, **очень ценится**.

1. Сделайте "Fork" проекта
2. Создайте свою ветку с "фичей" (`git checkout -b feature/AmazingFeature`)
3. Закомите свои изменения (`git commit -m 'Add some AmazingFeature'`)
4. Запуште это в ветку (`git push origin feature/AmazingFeature`)
5. Откройте "пул реквест"



<!-- LICENSE -->
## Лицензия

Распространяется под GNU GPL v3. Дополнительные сведения см. в разделе `LICENSE`.

<div>Иконка сделана <a href="https://www.freepik.com" title="Freepik">Freepik</a> от <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

<!-- CONTACT -->
## Contact

Роман - [@De_Grace](https://t.me/De_Grace) - Telegram

Ссылка на проект: [https://github.com/DoctorFreed/SortFiles](https://github.com/DoctorFreed/SortFiles)



<!-- ACKNOWLEDGEMENTS -->
## Благодарность

* [Othneil Drew](https://github.com/othneildrew/Best-README-Template) за дико крутой README шаблон!
* [Flaticon](https://www.flaticon.com/) за иконку для проекта!






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DoctorFreed/SortFiles.svg?style=for-the-badge
[contributors-url]: https://github.com/DoctorFreed/SortFiles/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DoctorFreed/SortFiles.svg?style=for-the-badge
[forks-url]: https://github.com/DoctorFreed/SortFiles/network/members
[stars-shield]: https://img.shields.io/github/stars/DoctorFreed/SortFiles.svg?style=for-the-badge
[stars-url]: https://github.com/DoctorFreed/SortFiles/stargazers
[issues-shield]: https://img.shields.io/github/issues/DoctorFreed/SortFiles.svg?style=for-the-badge
[issues-url]: https://github.com/DoctorFreed/SortFiles/issues
[license-shield]: https://img.shields.io/github/license/DoctorFreed/SortFiles.svg?style=for-the-badge
[license-url]: https://github.com/DoctorFreed/repo/blob/master/LICENSE.txt
