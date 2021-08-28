import chromedriver_binary # nopa
from selenium import webdriver
def driver_init():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    print('connectiong to remote browser...')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.get('https://qiita.com')

print(driver.current_url)
driver.quit()