#program to access upcoming python events and time with selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

#to keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#opens python.org tab
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# tapping into the timetag; first using Xpath of class="menu" and then again finding timetag
# under class menu using css selector (inspect python.org upcoming events)
time_tags = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').find_elements(By.CSS_SELECTOR, value="li time")
time_list = [time.get_attribute("datetime").split("T")[0] for time in time_tags ]

# similarly tapping into anchor tag the same way which has the name of event
anchor_tags = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').find_elements(By.CSS_SELECTOR, value="li a")
event_list = [event.text for event in anchor_tags]

#creating a events dictionary of format{0:{"time":"", "name":""}, 1:{.....}, ....,5:{...}}
events ={}
for n in range(len(event_list)):
    event = {
        "time":time_list[n],
         "name":event_list[n]
    }
    events[n] = event

print(events)

#to quit the entire chrome browser
driver.quit()

