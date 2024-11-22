from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input("Press enter after scanning QR code")
sleep(3)
new_chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/header/header/div/span/div/span/div[1]/div/span').click()
sleep(2)
search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div/p')
sleep(1)
search.send_keys("+972548082093")
sleep(1)
search.send_keys(Keys.ENTER)
sleep(1)
msg = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
sleep(2)
msg.send_keys("Hi, how are you?")
sleep(2)
driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span').click()
# +972 54-721-5727
# +972 53-373-5610
sleep(5)
driver.quit()