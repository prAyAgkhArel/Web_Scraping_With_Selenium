#scraping wikipedia main page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chorme_options = webdriver.ChromeOptions()
chorme_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chorme_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

#article count is the element that has anchor tag
# clicking to the link behind the text of anchor tag
#article_count.click()

#other method to click on the link behind the text of anchor tag
# lets tap in into community portal which is one of text of anchor tag of wikipedia
community_portal = driver.find_element(By.LINK_TEXT, value="Community portal")
#community_portal.click()

#searching through the search bar by passing keyboard input in wikipedia
# search = driver.find_element(By.NAME, value="search")
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python Programming")
search.send_keys(Keys.ENTER)
#Enter is the return key after passing input to search


#driver.quit()