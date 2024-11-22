from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# driver.get("https://google.com")
# sleep(5)
# driver.execute_script("window.open('https://ksp.co.il/web/cat/31635..271', '_blank')")
# sleep(3)
# driver.switch_to.window(driver.window_handles[1])
# sleep(2)
# driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[4]/div/button[8]/p')
# sleep(5)
#
# driver.execute_script("window.open('https://www.walla.co.il', '_blank')")
# sleep(3)
# cnt=1
# for window_handle in driver.window_handles:
#     driver.switch_to.window(window_handle)
#     sleep(5)
#     driver.get_screenshot_as_file(f"page_{cnt}.png")
#     cnt += 1

driver.get("https://vinothqaacademy.com/alert-and-popup/")
driver.find_element(By.NAME, 'alertbox').click()
sleep(1)
alert_object = driver.switch_to.alert
msg = alert_object.text
print(msg)
alert_object.accept()
sleep(1)
driver.find_element(By.NAME, 'confirmalertbox').click()
alert_object.dismiss()
sleep(5)

driver.find_element(By.NAME, 'promptalertbox1234').click()
alert_object.send_keys("You are a stupid automation program!")
sleep(5)
alert_object.accept()
sleep(4)
quit()
