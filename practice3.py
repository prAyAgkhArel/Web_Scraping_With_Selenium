from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,value="fName")
last_name = driver.find_element(By.NAME,value="lName")
email = driver.find_element(By.NAME,value="email")


first_name.send_keys("Prayag")
last_name.send_keys("Kharel")
email.send_keys("notesscience001@gmail.com")


sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()

