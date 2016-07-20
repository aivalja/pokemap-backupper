import time
from selenium import webdriver
driver = webdriver.Firefox()
firefoxProfile = webdriver.FirefoxProfile();
"""
firefoxProfile.set_preference("browser.download.folderList",2);
firefoxProfile.set_preference("browser.download.manager.showWhenStarting",False);
firefoxProfile.set_preference("browser.download.dir","B:");
firefoxProfile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/vnd.google-earth.kmz')
"""
driver.get("https://google.com")
while(True):
    driver.get("https://www.google.com/maps/d/kml?mid=1Po0ktZDG3HoIVhraT9-KPAIoyeQ&forcekml=1&cid=mp&cv=LLS4f3GpivQ.en.")
    driver.get("https://www.google.com/maps/d/kml?authuser=0&mid=1EpbuKPAlRGW25hQaz9-ZaMQhPBE&forcekml=1&cid=mp&cv=LLS4f3GpivQ.en.")
    time.sleep(1800)
driver.quit()
