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
driver.get('https://zenn.dev')
print(driver.find_element_by_xpath('//*[@id="tech-trend"]/div/div[2]/div/div[1]/article/div/a[1]/h2').text)


print(driver.current_url)
driver.quit()