from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

def tag_getir(id):
    return driver.find_element(By.ID, value=id)


cookie_tag = tag_getir("cookie") #driver.find_element(By.ID, value="cookie")

while True:
    cookie_tag.click()
    cursor_tag = tag_getir("buyCursor")
    grandma_tag = tag_getir("buyGrandma")
    factory_tag = tag_getir("buyFactory")
    mine_tag = tag_getir("buyMine")
    shipment_tag = tag_getir("buyShipment")
    alchemy_tag = tag_getir("buyAlchemy lab")
    portal_tag = tag_getir("buyPortal")
    time_machine_tag = tag_getir("buyTime machine")
    if float(cursor_tag.text.replace("\n", " ").split(" ")[2]) < float(grandma_tag.text.replace("\n", " ").split(" ")[2]):
        cursor_tag.click()
    elif float(grandma_tag.text.replace("\n", " ").split(" ")[2]) < float(factory_tag.text.replace("\n", " ").split(" ")[2]):
        grandma_tag.click()
    elif float(factory_tag.text.replace("\n", " ").split(" ")[2]) < float(mine_tag.text.replace("\n", " ").split(" ")[2]):
        factory_tag.click()
    elif float(mine_tag.text.replace("\n", " ").split(" ")[2]) < float(shipment_tag.text.replace("\n", " ").split(" ")[2]):
        mine_tag.click()
    elif float(shipment_tag.text.replace("\n", " ").split(" ")[2]) < float(alchemy_tag.text.replace("\n", " ").split(" ")[2]):
        shipment_tag.click()
    elif float(alchemy_tag.text.replace("\n", " ").split(" ")[2]) < float(portal_tag.text.replace("\n", " ").split(" ")[2]):
        alchemy_tag.click()
    elif float(portal_tag.text.replace("\n", " ").split(" ")[2]) < float(time_machine_tag.text.replace("\n", " ").split(" ")[2]):
        portal_tag.click()
    else:
        time_machine_tag.click()
















