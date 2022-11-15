import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)

driver.get(r'')
time.sleep(1)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select("")


print(thumbnails.text)
