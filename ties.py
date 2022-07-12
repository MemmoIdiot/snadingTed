from time import sleep

from pywinauto import application, findwindows
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from WindowFinder import WindowFinder

option: Options = Options()
option.add_experimental_option("debuggerAddress", "localhost:8989")

driver: Chrome = Chrome(
    service=Service(ChromeDriverManager().install()),
    #!executable_path=config.chromeDriver,
    options=option
    #! chrome_options=option
)

#TODO Immagini

driver.find_element(
    By.XPATH,
    "//button[@class='Button_button__1HmfN Button_primary__7rvYY Button_inline__3k2so Button_truncated__3pQ92 Button_icon-left__1QZEf']"
).click()
sleep(2)
#! app = application.Application()
#! w_handle = app.connect(title='Apri')
#! window = app.window_(handle=w_handle)
#! from pprint import pprint
#!
#! pprint(vars(window))
#! #! ctrl = window['Name']
#! #! ctrl.SetText(r'C:\Users\Memmo\Dropbox\Screenshot\2019_05_20_16_31_38.jpg')
#! #! ctrl = window['OK']
#! #! ctrl.Click()
#! exit()

# * title
driver.find_element(By.XPATH, "//input[@id='title']").send_keys('Title')
# * description
driver.find_element(By.XPATH,
                    "//textarea[@id='description']").send_keys('Description')

# * category (🇮🇹 Cravatte e fazzoletti da taschino)
driver.find_element(By.XPATH, "//input[@id='catalog_id']").click()
driver.find_element(By.XPATH, "//div[@id='catalog-5']").click()
driver.find_element(By.XPATH, "//div[@id='catalog-82']").click()
driver.find_element(By.XPATH, "//div[@id='catalog-93']").click()

# * brand
driver.find_element(By.XPATH,
                    "//input[@id='brand_id']").send_keys(r'A very cool brand')

# * status: excellent (🇮🇹 Ottimo)
driver.find_element(By.XPATH, "//input[@id='status_id']").click()
driver.find_element(By.XPATH, "//span[@aria-labelledby='status-2']").click()

#TODO settare colori

# * price
driver.find_element(By.XPATH, "//input[@id='price']").send_keys(10)  # * €

#* package size: little (🇮🇹 Piccola)
driver.find_element(By.XPATH,
                    "//span[@aria-labelledby='package-size-1']").click()
