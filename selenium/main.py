#import chromedriver_binary # nopa
from get_chrome_driver import GetChromeDriver
from selenium import webdriver

get_driver = GetChromeDriver()
get_driver.install()

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    print('connectiong to remote browser...')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.get('https://qiita.com')

print(driver.current_url)
driver.quit()