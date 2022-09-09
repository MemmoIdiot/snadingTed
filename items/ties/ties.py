from os import listdir
from os.path import join
from time import sleep
from typing import List

from Data import Data
from items.Colors import Colors
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def job():
    option: Options = Options()
    option.add_experimental_option("debuggerAddress", "localhost:8989")

    driver: Chrome = Chrome(service=Service(ChromeDriverManager().install()),
                            options=option)

    tie_brand: str
    colors: List[str]

    # * images
    for tie in listdir(Data.PATH):
        driver.get("https://www.vinted.it/items/new")
        for pic in sorted(listdir(join(Data.PATH, tie))):
            driver.find_element(By.XPATH,
                                "//div[@id='photos']/input").send_keys(
                                    join(Data.PATH, tie, pic))

            sleep(3)

        tie_brand = tie.split(' - ')[0]
        colors = tie.split(' - ')[1].split(' ')

        # * title
        driver.find_element(
            By.XPATH,
            "//input[@id='title']").send_keys(f'Cravatta {tie_brand}')
        sleep(1)

        # * description
        driver.find_element(By.XPATH,
                            "//textarea[@id='description']").send_keys(
                                Data.DESCRIPTION)
        sleep(1)

        # * (🇮🇹 Cravatte e fazzoletti da taschino)
        driver.find_element(By.XPATH, "//input[@id='catalog_id']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[@id='catalog-5']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[@id='catalog-82']").click()
        sleep(1)
        driver.find_element(By.XPATH, "//div[@id='catalog-93']").click()
        sleep(1)

        # * brand
        brand = driver.find_element(By.XPATH, '//*[@id="brand_id"]')
        brand.clear()
        brand.send_keys("Annuncio senza brand")
        brand.click()

        # * status: excellent (🇮🇹 Ottimo)
        driver.find_element(By.XPATH, "//input[@id='status_id']").click()
        sleep(1)
        driver.find_element(By.XPATH,
                            "//span[@aria-labelledby='status-2']").click()
        sleep(1)

        # * colors
        driver.find_element(By.XPATH, '//*[@id="color"]').click()
        sleep(0.5)
        for c in colors:
            driver.find_element(By.XPATH, Colors.COLORS_SELECTOR[c]).click()
            sleep(1)
        driver.find_element(By.XPATH, '//*[@class="site-content"]').click()
        sleep(1)

        # * price
        driver.find_element(By.CSS_SELECTOR, '#price').send_keys(Data.PRICE)

        # * package size: little (🇮🇹 Piccola)
        driver.find_element(
            By.XPATH, "//span[@aria-labelledby='package-size-1']").click()
        sleep(1)

        # * (Carica 🇮🇹)
        driver.find_element(
            By.XPATH,
            "//button[@data-testid='upload-form-save-button']").click()
        sleep(5)
