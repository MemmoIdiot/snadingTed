#File to start the Chrome window


def find_files(filename, search_path):
    from os.path import join
    from os import walk
    result = ""
    for root, dir, files in walk(search_path):
        if filename in files:
            result += str(join(root, filename))

    return result


def check_chrome_profile(directory_path):
    from os.path import exists
    from os import mkdir

    if not exists(directory_path):
        mkdir(directory_path)


def start(func):

    def wrapper():
        from subprocess import Popen
        from time import sleep
        from json import load

        file = open('data.json')

        data = load(file)
        chrome_datas = data["chrome_datas"]
        bot_data = data["bot_css_selector"]

        chrome_profile = chrome_datas["chrome_profile_start_path"]

        path_1 = find_files(chrome_datas["chrome"],
                            chrome_datas["chrome.exe_start_path"])
        check_chrome_profile(chrome_profile)

        Popen(
            f'{path_1} --remote-debugging-port=8989 --user-data-dir=\"{chrome_profile}\"'
        )
        sleep(1)

        func(bot_data)

    return wrapper()
