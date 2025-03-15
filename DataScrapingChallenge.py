from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")

dates = driver.find_elements(By.CLASS_NAME, value="medium-widget.event-widget.last time")
events = driver.find_elements(By.CLASS_NAME, value="medium-widget.event-widget.last ul.menu a")
upcoming_events = {}
for i in range(len(dates)):
    upcoming_events[i] = {
        "time": dates[i].text,
        "event": events[i].text
    }
print(upcoming_events)


driver.quit()