from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)

driver.get('https://www.limeroad.com/t-shirts-workout-in-style-by-kanika-crystal-st6093799ff47b7008304becba')
print(1)

dress = driver.find_element_by_xpath('//*[@id="17605154"]')
dress.click()

size = driver.find_element_by_xpath('//*[@id="alSz"]/div[3]')
size.click()

shop = driver.find_element_by_xpath(
    '//*[@id="views"]/div/div/div[3]/div[1]/div[4]/div[4]/div[3]/div[2]')
shop.click()
