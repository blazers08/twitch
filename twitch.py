from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver 2')

driver.get('https://www.twitch.tv/xargon0731/videos?filter=archives&sort=time')

sleep(5)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
html = driver.page_source
# print(html)

driver.quit()


soup = BeautifulSoup(html, 'html.parser')
# rint(soup.prettify())
a = soup.find('div', 'tw-pd-b-1 tw-pd-x-4').find('div','tw-mg-t-2').find('div', 'tw-flex-wrap tw-tower tw-tower--300 tw-tower--gutter-xs').find_all('div', 'tw-mg-b-2')
# print(a)
for div in a:
   title = div.find('h3')['title']
   href = div.find('a')['href']
   print('title:', title)
   print('href:', href)

# print(a)
# tw-mg-b-2