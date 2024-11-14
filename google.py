from typing import final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
sleep(5)
# search_box = driver.find_element(By.ID, 'APjFqb')
# search_box.send_keys("python selenium")
# driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
# sleep(6)

driver.find_element(By.LINK_TEXT, 'Gmail').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div/div[4]/gws-dropdown-button/div').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div/div[4]/gws-dropdown-button/a[1]/span').click()
sleep(2)
firstname = driver.find_element(By.ID, 'firstName')
firstname.send_keys("Sancho Pansa")
driver.find_element(By.XPATH, '//*[@id="collectNameNext"]/div/button/span').click()
sleep(2)
month = Select(driver.find_element(By.ID, 'month'))
month.select_by_value('11')
sleep(5)
driver.quit()  # exit from webdriver fully