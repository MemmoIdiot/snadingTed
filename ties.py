from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

option: Options = Options()
option.add_experimental_option("debuggerAddress", "localhost:8989")

driver: Chrome = Chrome(
    service=Service(ChromeDriverManager().install()),
    #!executable_path=config.chromeDriver,
    options=option
    #! chrome_options=option
)
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

#TODO settare colori

# * price
driver.find_element(By.XPATH, "//input[@id='price']").send_keys(10)

#* package size: little (🇮🇹 Piccola)
driver.find_element(By.XPATH,
                    "//span[@aria-labelledby='package-size-1']").click()
