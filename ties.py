from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pyautogui import write, press
from starter import start
from os import listdir
from os.path import (
    join,
    isfile,
)


def get_images(directory_path):
    images = ""
    for filename in listdir(directory_path):
        f = join(directory_path, filename)
        if isfile(f):
            imgae_name = f.replace(f"{directory_path}\\", "")
            images += f'\"{imgae_name}\" '
            print(images)

    return directory_path + "\\" + images


@start
def main(bot_data):

    option: Options = Options()
    option.add_experimental_option("debuggerAddress", "localhost:8989")

    driver: Chrome = Chrome(service=Service(ChromeDriverManager().install()),
                            options=option)

    driver.maximize_window()
    driver.get("https://www.vinted.it/items/new")

    #image
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, bot_data["image_button"]).click()
    sleep(1)

    directory_path = "C:\\Users\\Paolo\\OneDrive\\altro\\Immagini\\test"
    write(get_images(directory_path))
    press('enter')

    # * title
    driver.find_element(By.CSS_SELECTOR, bot_data["title"]).send_keys('Title')
    # * description
    driver.find_element(By.CSS_SELECTOR,
                        bot_data["description"]).send_keys('Description')

    # * (🇮🇹 Cravatte e fazzoletti da taschino)
    driver.find_element(By.CSS_SELECTOR, bot_data["item"]["category"]).click()
    driver.find_element(By.CSS_SELECTOR, bot_data["item"]["man"]).click()
    driver.find_element(By.CSS_SELECTOR,
                        bot_data["item"]["accessories"]).click()
    driver.find_element(By.CSS_SELECTOR, bot_data["item"]["ties"]).click()

    # * brand
    driver.find_element(By.CSS_SELECTOR,
                        bot_data["brand"]).send_keys(r'A very cool brand')

    # * status: excellent (🇮🇹 Ottimo)
    driver.find_element(By.CSS_SELECTOR,
                        bot_data["status"]["status_id"]).click()
    driver.find_element(By.CSS_SELECTOR,
                        bot_data["status"]["excellent"]).click()

    #colors
    driver.find_element(By.CSS_SELECTOR, bot_data["color"]["selector"]).click()
    #Selector of first 17 colors : color-(1,17) .Checkbox_button__34dpJ
    #Selector of last 10 colors : #color-(20,30) > div.Cell_suffix__1Yku3
    driver.find_element(By.CSS_SELECTOR, bot_data["color"]["color1"]).click()
    #driver.find_element(By.CSS_SELECTOR, "#color-1 > div.Cell_suffix__1Yku3 > label > span").send_keys("Nero")

    driver.find_element(By.CSS_SELECTOR, bot_data["color"]["color2"]).click()
    driver.find_element(By.CSS_SELECTOR,
                        bot_data["color"]["exit_click"]).click()
    # * price
    driver.find_element(By.CSS_SELECTOR, bot_data["price"]).send_keys(10)

    #* package size: little (🇮🇹 Piccola)
    driver.find_element(By.CSS_SELECTOR, bot_data["package_size"]).click()
