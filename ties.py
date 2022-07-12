from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pyautogui import write,press



option: Options = Options()
option.add_experimental_option("debuggerAddress", "localhost:8989")

driver: Chrome = Chrome(
    service=Service(ChromeDriverManager().install()),
    options=option
)

driver.get("https://www.vinted.it/items/new")
#image
sleep(1)
driver.find_element(By.CSS_SELECTOR,"#photos > div.Cell_cell__3V4ao.Cell_wide__1ukxw > div > div > div > div.media-select__input > div > button").click()
sleep(1)
write('C:\\Users\\Paolo\\OneDrive\\altro\\Immagini\\images.jpg') 
press('enter')

# * title
driver.find_element(By.XPATH,
                    "//input[@id='title']").send_keys('Title')
# * description
driver.find_element(By.XPATH,
                    "//textarea[@id='description']").send_keys('Description')

# * (🇮🇹 Cravatte e fazzoletti da taschino)
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

#colors
driver.find_element(By.XPATH, "//*[@id='color']").click()
#Selector of first 17 colors : color-(1,17) .Checkbox_button__34dpJ
#Selector of last 10 colors : #color-(20,30) > div.Cell_suffix__1Yku3 
driver.find_element(By.CSS_SELECTOR, "#color-1 .Checkbox_button__34dpJ").click()
driver.find_element(By.CSS_SELECTOR, "#color-5 .Checkbox_button__34dpJ").click()
driver.find_element(By.CSS_SELECTOR, ".c-input:nth-child(7) > .c-input__title").click()
# * price
driver.find_element(By.XPATH, "//input[@id='price']").send_keys(10)

#* package size: little (🇮🇹 Piccola)
driver.find_element(By.XPATH,
                    "//span[@aria-labelledby='package-size-1']").click()