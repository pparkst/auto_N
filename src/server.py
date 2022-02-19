import time
import selenium
import subprocess
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options


def get_selenium_driver(headless=True):
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('lang=en')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    return driver



def get_original_chrome_driver():
    subprocess.call('Google\\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"', shell=True)
    time.sleep(5)
    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=option)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=option)

    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)

    return driver



def n_login():
    btn_login = driver.find_element_by_xpath('//*[@data-qa="top-nav-login-button"]')
    btn_login.click()

    input_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "j_username"))
    )
    time.sleep(2)
    input_id.send_keys("aaa@gmail.com")
    time.sleep(2)
    driver.find_element_by_id("j_password").send_keys("123")
    driver.find_element_by_class_name("uk-form-large").submit()


try:
    driver = get_original_chrome_driver()
    driver.get('https://www.nike.com/kr/launch/')
    n_login()
except:
    time.sleep(10)
    driver.close()
finally:
    time.sleep(10)