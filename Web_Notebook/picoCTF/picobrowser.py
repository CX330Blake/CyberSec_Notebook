from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

my_user_agent = "picobrowser"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-agent={my_user_agent}")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://jupiter.challenges.picoctf.org/problem/28921/flag"

driver.get(url)
time.sleep(1337)
