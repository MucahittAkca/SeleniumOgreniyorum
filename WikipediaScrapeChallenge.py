from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value="//*[@id='articlecount']/ul/li[2]/a[1]")

#Tıklama
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

#Yazma
driver.maximize_window()
searchbar = driver.find_element(By.NAME, value="search")
searchbar.send_keys("python", Keys.ENTER)
searchbar.send_keys(Keys.ENTER)











