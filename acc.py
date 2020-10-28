from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time

url = 'https://www.playstation.com/en-us'

driver = webdriver.Chrome('chromedriver.exe')

driver.get(url)

#driver.set_page_load_timeout(10)

time.sleep(2)

driver.find_element_by_xpath('//*[@class="sb-skeleton-signin-button"]').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@class="secondary-button row-button text-button"]').click()

time.sleep(5)

driver.find_element_by_xpath('//span[@class="caption"]').click()
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='caption']"))).click()

time.sleep(10)

slct = Select(driver.find_element_by_xpath("//select[@class='pulldown-text icon-pulldown-arrow ']"))
slct.select_by_value("CA")

time.sleep(10)

mnth = Select(driver.find_element_by_xpath("//select[@title='Month']"))
mnth.select_by_value("2")

time.sleep(2)

day = Select(driver.find_element_by_xpath("//select[@title='Day']"))
day.select_by_value("4")

time.sleep(2)

year = Select(driver.find_element_by_xpath("//select[@title='Year']"))
year.select_by_value("1990")

time.sleep(2)

driver.find_element_by_xpath('//*[@class="content-area"]').click()

time.sleep(5)

#Account info
#driver.find_element_by_id("ember442").send_keys("lazy@maildrop.cc")


mail = driver.find_element_by_id("ember442")
text = 'lazy@maildrop.cc'

for character in text:
    mail.send_keys(character)
    time.sleep(0.2)

time.sleep(1)

#driver.find_element_by_id("ember446").send_keys('beyondHuman1298')

passwrd = driver.find_element_by_id('ember446')
text2 = "beyondhuman1298"

for charachter in text2:
    passwrd.send_keys(charachter)
    time.sleep(0.2)

time.sleep(1)

#driver.find_element_by_id("ember448").send_keys('beyondHuman1298')

passwrd2 = driver.find_element_by_id('ember448')
text3 = "beyondhuman1298"

for charachter in text3:
    passwrd2.send_keys(charachter)
    time.sleep(0.2)

time.sleep(4)

driver.find_element_by_class_name("next-button").click()





#driver.find_element_by_xpath('//*[@class="next-button text-button"]').find_element_by_xpath('//*[@class="content-area"]').click()


