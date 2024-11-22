from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

url = "https://ksp.co.il/web/cat/31635..271"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
sleep(10)

while True:
    # get the current page height with scroll down position
    page_height = driver.execute_script("return document.body.scrollHeight")
    # print(page_height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    driver.implicitly_wait(10)
    sleep(5)
    # get the new height of the page
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == page_height:
        break
    page_height = new_height
    try:
        desired = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[4]/div/div/div[2]/div[2]/div[3]/div[1]/div[38]/div/div[5]/h3/a')
        if desired:
            href_elem = desired.get_attribute("href")
            # desired.click()
            driver.get(href_elem)
            break
    except NoSuchElementException:
        pass

sleep(2)


sleep(5)
driver.quit()