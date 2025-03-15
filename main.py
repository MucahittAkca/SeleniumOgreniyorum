from selenium import webdriver
from selenium.webdriver.common.by import By

#program sonlanınca chrome açık kalmalı
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#driver.get("https://www.amazon.com")



#driver.close() #tek bir sekmeyi, açtığımız ilgili sekmeyi kapatı
#driver.quit() #Tüm tarayıcıdan çıkacaktır.



###  AmazonPriceTracker'ın selenium ile daha kolay versiyonu ###


#driver.get("https://www.amazon.com.tr/Hawk-Gaming-Chair-Oyuncu-Koltu%C4%9Fu/dp/B09QCZB2YC?pd_rd_w=phVk5&content-id=amzn1.sym.431886a5-f219-464d-a7c5-c68c12312177&pf_rd_p=431886a5-f219-464d-a7c5-c68c12312177&pf_rd_r=P0ZKK75MBGS8JXQY6EPW&pd_rd_wg=74wrd&pd_rd_r=12d7d08d-d678-4211-b514-2a74dae4870c&pd_rd_i=B09QCZB2YC&ref_=pd_hp_d_btf_unk_B09QCZB2YC&th=1")

#ücret = driver.find_element(By.CLASS_NAME, "a-price-whole")
#kuruş = driver.find_element(By.CLASS_NAME, "a-price-fraction")
#print(ücret.text + "." + kuruş.text) #8.39900



#Python sitesinde name özelliği ile arama
driver.get("https://www.python.org")
searchbar = driver.find_element(By.NAME, value="q")
print(searchbar.tag_name) # "input"
print(searchbar.get_attribute("placeholder")) # "search"
button = driver.find_element(By.ID, value="submit")
print(button.size) # "{'height': 40, 'width': 46}"


documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

#Xpath ile bulma
bug_link = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")

print(bug_link.text)

















driver.quit()