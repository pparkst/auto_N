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
        
        # use proxy required open the 9150 port (e.g. tor
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

    input_id = WebDriverWait(driver, 400).until(
        EC.presence_of_element_located((By.ID, "loginId"))
    )

    KEY = config.K_KEY
    time.sleep(2)
    input_id.send_keys(KEY.USERNAME)
    time.sleep(2)
    driver.find_element_by_id("loginPwd").send_keys(KEY.PASSWORD)
    time.sleep(1)
    driver.find_element_by_id("formLogin").submit()
    time.sleep(2)



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


def k_product(driver, itemName):
    driver.get("https://www.kasina.co.kr/goods/populate.php")
    #"//div[@class='fc-day-content' and text()='15']"

    # arr_spn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='item_name']"))
    # )

    arr_spn = driver.find_elements_by_class_name("item_name")

    print(arr_spn)

    for spn in arr_spn:
        if itemName in spn.text:
            spn.click()
            break



    # for spn in arr_spn:
    #     print(spn)
    #     print(spn.text)

def k_selectSizeAndCheckout(driver):
    print("k_selectSizeAndCheckout")

    #chosen-container
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "chosen-container"))
    )
    
    # select2 = Select(driver.find_element_by_name("//select[@name='optionSnoInput']"))

    # print(select2)

    # select2.select_by_index(2)
    driver.execute_script("$('[name=optionSnoInput] option:eq(2)').prop('selected', true); $('[name=optionSnoInput]').trigger('onchange')")
    time.sleep(2)
    btn_buy = driver.find_element_by_class_name("btn_add_order")
    btn_buy.click()
    
    print("End")
    # print(opt_arr.text)
    # opt_arr.click()


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
def k_checkout(driver):
    print("k_checkout")
    #driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #phoneNum

    # input_phoneNum = WebDriverWait(driver, 400).until(
    #     EC.presence_of_element_located((By.ID, "phoneNum"))
    # )
    # input_phoneNum.send_keys("\n")

    chk_noti = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "termAgree_orderCheck"))
    )

    chk_kakaoPay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "settleKind_pk"))
    )
    print("chk_noti ", chk_noti)
    print("chk_kakaoPay ", chk_kakaoPay)

    chk_kakaoPay.click()

    chk_noti.click()

    btn_checkout = driver.find_element_by_class_name("btn_order_buy")
    btn_checkout.click()


def inicisPopup(driver):
    time.sleep(2)
    driver.switch_to_default_content()

    btn_next = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "CardBtn"))
    )

    btn_agree = driver.find_element_by_id("inputAll")
    btn_agree.click()

    btn_kakaoPay = driver.find_element_by_id("payCode10")
    btn_kakaoPay.click()
    
    btn_next.click()


try:
    start = time.time()

    driver = get_original_firefox_driver()

    k_login(driver)
    k_product(driver, "NIKE DUNK HI")
    k_selectSizeAndCheckout(driver)
    k_checkout(driver)
    #inicisPopup(driver)
    #n_login()
except Exception as e:
    print("Exception", e)
    driver.close()
finally:
    time.sleep(60)
    driver.quit()
    end = time.time()
    print(format(end-start))
