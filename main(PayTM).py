from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#download chromedriver from here "https://sites.google.com/a/chromium.org/chromedriver/downloads" and move it to this path
path="C:\\Python27\\selenium\\webdriver\\chromedriver.exe"

options = webdriver.ChromeOptions()
#options.binary_location = 'C:\Python27\selenium\webdriver\chromedriver.exe'
options.add_argument('headless')

options.add_argument('disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome(path)
_from=raw_input("From: ")
_to=raw_input("To: ")
_date=raw_input("Date: YYYY-MM-DD: ")
link="https://paytm.com/bus-tickets/search/{}%20/{}/{}/1".format(_from,_to,_date)
driver.get(link)
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@class='_3WeX']")))
#time.sleep(20)
result_all=driver.find_elements_by_xpath("//*[@class='_1YcT ghuP']")
result_price=driver.find_elements_by_xpath("//*[@class='_1YcT HB24']")
all_links=[]
#for element in result:
	#if 'tags' not in element.get_attribute('href'):
#	all_links.append(element.get_attribute('div'))

#print len(all_links)
#print len(result)
#print all_links[0]
for i,j in zip(result_all,result_price):
	print "Bus ",i.text," Price ",j.text
driver.close()
#driver.quit()