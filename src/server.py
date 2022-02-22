import time
import selenium
import subprocess
import chromedriver_autoinstaller
import config

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
    try:
        #subprocess.call('Google\\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"', shell=True)
        #time.sleep(5)
        option = Options()

        # tor
        option.add_argument("--proxy-server=socks5://127.0.0.1:9150")
        
        # chrome debugger mode
        #option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_ver = 98

        print("Go Driver")
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=option)
    except Exception as e:
        print(e)
        print("err Driver")
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=option)

    driver.implicitly_wait(10)

    return driver

def get_original_firefox_driver():
    try:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", '127.0.0.1')
        profile.set_preference("network.proxy.socks_port", 9150)
        profile.set_preference("network.proxy.socks_remote_dns", False)
        profile.update_preferences()
        
        # use proxy
        #driver = webdriver.Firefox(executable_path="./driver/geckodriver", firefox_profile=profile)

        # just browser
        driver = webdriver.Firefox(executable_path="./driver/geckodriver")
        driver.implicitly_wait(10)

    

        # PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # driver = webdriver.Chrome(chrome_options=chrome_options)
    except Exception as e:
        print("get_original_firefox_driver")
        print(e)

    return driver

def k_login(driver):
    driver.get("https://www.kasina.co.kr/member/login.php")

    input_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginId"))
    )

    KEY = config.K_KEY
    time.sleep(2)
    input_id.send_keys(KEY.USERNAME)
    time.sleep(2)
    driver.find_element_by_id("loginPwd").send_keys(KEY.PASSWORD)
    time.sleep(1)
    driver.find_element_by_id("formLogin").submit()



def n_login(driver):
    driver.get("https://www.nike.com/kr/launch/")
    btn_login = driver.find_element_by_xpath('//*[@data-qa="top-nav-login-button"]')
    btn_login.click()
    KEY = config.N_KEY

    input_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "j_username"))
    )
    time.sleep(2)
    input_id.send_keys(KEY.USERNAME)
    time.sleep(2)
    driver.find_element_by_id("j_password").send_keys(KEY.PASSWORD)
    driver.find_element_by_class_name("uk-form-large").submit()


def k_product(driver):
    driver.get("https://www.kasina.co.kr/goods/populate.php")
    #"//div[@class='fc-day-content' and text()='15']"

    # arr_spn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='item_name']"))
    # )

    arr_spn = driver.find_elements_by_class_name("item_name")

    print(arr_spn)

    for spn in arr_spn:
        if "TERRASCAPE" in spn.text:
            spn.click()
            break



    # for spn in arr_spn:
    #     print(spn)
    #     print(spn.text)

def k_selectSizeAndCheckout(driver):
    print("k_selectSizeAndCheckout")

    select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "chosen-select"))
    ))
    #select = driver.find_element_by_name("optionSnoInput")
    print(select)

    opt_arr = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@class='chosen-select']//option[contains(@value,'240')]"))
    )
    print(opt_arr.text)
    opt_arr.click()



    

                    # $("[name='optionSnoInput'] option:eq(2)").prop("selected", true)
                    # $("[name='optionSnoInput']").trigger("onchange")


    # #??
    # #opt_arr = select.find_elements_by_css_selector("*")
    # time.sleep(3)
    # print(opt_arr)
    # print(opt_arr.text)
    # opt_arr.click()

    # for opt in opt_arr:
    #     val = opt.get_attribute("value")
    #     length = len(val)
    #     if "240" in val[length-3 : length]:
    #         print(val)
    #         opt.click()


try:
    start = time.time()
    driver = get_original_firefox_driver()
    #k_login(driver)
    k_product(driver)
    k_selectSizeAndCheckout(driver)
    #n_login()

    end = time.time()
    print(format(end-start))
except Exception as e:
    print("Exception", e)
    driver.close()
finally:
    time.sleep(10)
    driver.quit()
    print("finally")